import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Ortam değişkenlerini yükle
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Google API key bulunamadı. .env dosyasını kontrol et.")

# --- Excel dosyasını oku
tarif_df = pd.read_excel("yemekchatbot_200ornek.xlsx")  # Excel dosya adını kendine göre değiştir

# --- Sayfa başlığı ve açıklama
st.title("🍲 Yemek Tarifi Asistanı")
st.markdown("""
👋 **Hoş geldin!** Aşağıya yemek tarifleriyle ilgili bir soru yazarak tarif arayabilirsin.  
Örnek sorular:
- "Kolay ve hızlı bir tatlı önerir misin?"
- "Baklava tarifi nasıl yapılır?"
- "Malzemeleri şeker ve ceviz olan tatlılar neler?"
- "Hazırlaması 30 dakikadan kısa süren yemek tarifleri var mı?"
---
""")

# --- Excel'den veri -> Document
def yemek_to_document(row):
    text = f"""Yemek Adı: {row['Yemek Adı']}
Süre (dk): {row['Süre (dk)']}
Zorluk: {row['Zorluk']}
Malzemeler: {row['Malzemeler']}
Tarif: {row['Tarif']}"""
    return Document(page_content=text)

docs = [yemek_to_document(row) for _, row in tarif_df.iterrows()]
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = splitter.split_documents(docs)

# --- Vektör veritabanı
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    persist_directory="./chroma_yemek_db"
)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# --- LLM tanımı
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3,
    max_tokens=500
)

# --- Intent sınıflandırma zinciri
intent_prompt = PromptTemplate.from_template("""
Aşağıdaki kullanıcı cümlesinin hangi intent'e ait olduğunu belirle. 
Intent kategorileri:
- Yemek Önerisi
- Malzeme Sorgusu
- Süre Sorgusu
- Zorluk Sorgusu
- Selamlama
- Vedalaşma
- Bilinmeyen

Cümle: {soru}
Intent:
""")
intent_chain = intent_prompt | llm | StrOutputParser()

# --- RAG prompt
system_prompt = (
    "Sen yemek tarifleri hakkında bilgi veren bir asistansın.\n"
    "Aşağıdaki tarifleri kullanarak kullanıcı sorusunu yanıtla.\n"
    "Cevabın kısa, net ve bağlama dayalı olsun. Bilinmeyen bir şey varsa 'emin değilim' de.\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# --- Kullanıcıdan input al
query = st.text_input("🍽️ Yemek tarifleriyle ilgili bir sorunuz varsa buraya yazın:")

if query:
    intent = intent_chain.invoke({"soru": query})
    st.markdown(f"**🎯 Intent tespiti:** `{intent}`")

    if intent.lower() in ["yemek önerisi", "malzeme sorgusu", "süre sorgusu", "zorluk sorgusu"]:
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        response = rag_chain.invoke({"input": query})
        st.write(response["answer"])

    elif intent.lower() == "selamlama":
        st.write("Merhaba! Yemek tarifleri konusunda size nasıl yardımcı olabilirim? 🍳")

    elif intent.lower() == "vedalaşma":
        st.write("Afiyet olsun! Başka sorularınız olursa beklerim. 👋")

    else:
        st.write("Sorunuzu anlayamadım. Lütfen daha açık bir şekilde yazabilir misiniz?")
