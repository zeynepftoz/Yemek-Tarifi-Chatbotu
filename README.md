# 🍲 Yemek Tarifi Asistanı Chatbotu

Bu proje, yemek tarifleriyle ilgilenen kullanıcıların; malzeme, süre, zorluk gibi kriterlere göre tariflere ulaşmalarını sağlayan yapay zekâ destekli akıllı bir asistan uygulamasıdır.

---

## 🚀 Proje Amacı

Yemek yapmayı sevenlerin doğru ve hızlı tariflere erişimini kolaylaştırmak için geliştirilmiştir. Bu chatbot:

- Kullanıcının malzeme, süre veya zorluk sorgularına doğal dil ile yanıt verir.
- Tarif önerir, malzeme listesi sorgularını cevaplar.
- Kısa ve öz açıklamalarla tarifler hakkında bilgi sunar.
- Selamlaşma ve vedalaşma gibi etkileşimleri yönetir.

---

## 🧠 Kullanılan Teknolojiler

- **Python**  
- **Streamlit** – Kullanıcı arayüzü  
- **LangChain** – LLM ve RAG zinciri entegrasyonu  
- **Google Gemini 1.5 Pro (GenAI)** – Dil modeli  
- **Chroma** – Vektör tabanlı veri depolama ve arama  
- **GoogleGenerativeAIEmbeddings** – Metin embedding işlemleri  
- **dotenv (.env)** – API anahtar yönetimi  

---

## 📁 Dosya Yapısı

.
├── app.py # Chatbotun ana kodu
├── yemekchatbot_200ornek.xlsx # Tarif verilerini içeren Excel dosyası
├── .env # GOOGLE_API_KEY içeren gizli anahtar dosyası
├── chroma_yemek_db/ # Embedlenmiş veri tabanının saklandığı dizin
├── requirements.txt # Projede kullanılan Python paketleri


---

## 🔧 Kod Yapısına Genel Bakış

`app.py` dosyası Streamlit uygulamasını başlatır. Ana adımlar:

1. **Veri Yükleme**: Excel dosyasındaki yemek tarifleri okunur ve her satır bir LangChain `Document` nesnesine dönüştürülür.  
2. **Vektörleştirme**: Tariflerden oluşan belgeler Google GenAI Embed modeliyle embedlenir ve Chroma veritabanına kaydedilir.  
3. **Retriever Tanımı**: Benzer belgeleri bulabilmek için Chroma retriever ayarlanır.  
4. **LLM Bağlantısı**: Gemini 1.5 Pro modeli kullanılır.  
5. **Intent Sınıflandırma**: Kullanıcının sorduğu cümleye uygun intent belirlenir.  
6. **RAG Zinciri**: Eğer intent anlamlıysa (yemek önerisi, malzeme sorgusu vs.) özet bilgileriyle birlikte cevap üretilir.  
7. **UI**: Kullanıcı sorusunu girer, intent tanınır ve cevap görüntülenir.

---

## 📊 Veri Seti Formatı

| Yemek Adı | Hazırlanma Süresi (dk) | Zorluk Seviyesi | Malzemeler | Hazırlama Talimatları |
| --------- | ---------------------- | --------------- | ---------- | --------------------- |

Örnek Satır:

Baklava | 30 | Zor | Baklava yufkası, ceviz, şerbet | Baklava yufkaları arası ceviz konulur, şerbet dökülür.


---

## 🔍 Örnek Sorgular

- "Malzemeleri un ve yumurta olan tatlılar nelerdir?"  
- "Hazırlaması 20 dakikadan kısa olan yemek tarifleri var mı?"  
- "Kolay ve pratik bir çorba önerir misin?"  
- "Merhaba" → Selamlaşma cevabı alırsınız.

---

## 🔧 Kurulum

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
Proje klasöründe .env dosyası oluşturun ve içine API anahtarınızı yazın:
GOOGLE_API_KEY=your_api_key_here

Uygulamayı başlatın:
streamlit run app.py

## Neden bu chatbot?
Yemek tarifleri ararken zorlananlara, doğal dil ile sorularını sorup hızlıca cevaba ulaşabilecekleri bir asistan sunmak için geliştirildi.

Bu bot sayesinde:

Malzeme, süre ve zorluk gibi kriterlere göre filtreleme yapılabilir.

Kullanıcılar, aradıkları tarife kolayca ulaşabilir.

Pratik ve anlaşılır tarif önerileri sunulur.

