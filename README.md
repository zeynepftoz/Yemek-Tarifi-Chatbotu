# 🍲 Yemek Tarifi Asistanı Chatbotu

Bu proje, yemek tarifleriyle ilgilenen kullanıcıların; malzeme, süre, zorluk gibi kriterlere göre tariflere ulaşmalarını sağlayan yapay zekâ destekli akıllı bir asistan uygulamasıdır.

---

## 🚀 Proje Amacı

Günümüzde yemek yapmayı sevenlerin doğru ve hızlı tariflere erişimi önemlidir. Bu chatbot:

- Kullanıcının malzeme, süre veya zorluk sorgularına doğal dil ile yanıt verir.
- Tarif önerir, malzeme listesi sorgularını cevaplar.
- Kısa ve öz açıklamalarla tarifler hakkında bilgi sunar.
- Selamlaşma ve vedalaşma gibi etkileşimleri yönetir.

---

## 🧠 Kullanılan Teknolojiler

- Python  
- Streamlit – Kullanıcı arayüzü  
- LangChain – LLM ve RAG zinciri entegrasyonu  
- Google Gemini 1.5 Pro (GenAI) – Dil modeli  
- Chroma – Vektör tabanlı veri depolama ve arama  
- GoogleGenerativeAIEmbeddings – Metin embedding işlemleri  
- dotenv (.env) – API anahtar yönetimi  

---

## 📁 Proje Dosya Yapısı

.
├── app.py # Chatbotun ana kodu
├── yemekchatbot_200ornek.xlsx # Tarif verilerini içeren Excel dosyası
├── .env # GOOGLE_API_KEY içeren gizli anahtar dosyası
├── chroma_yemek_db/ # Embedlenmiş veri tabanının saklandığı dizin
├── requirements.txt # Projede kullanılan Python paketleri

yaml
Kopyala

---

## 🔧 Kurulum ve Çalıştırma

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
Proje klasöründe .env dosyası oluşturun ve içine API anahtarınızı yazın:

ini
Kopyala
GOOGLE_API_KEY=your_google_api_key_here
Uygulamayı başlatın:

bash
Kopyala
streamlit run app.py
Tarayıcıda açılan sayfada yemek tarifleriyle ilgili sorularınızı yazabilirsiniz.

📊 Veri Seti Formatı
Excel dosyasında şu sütunlar olmalıdır:

Yemek Adı	Hazırlanma Süresi (dk)	Zorluk Seviyesi	Malzemeler	Hazırlama Talimatları
Örnek: Baklava	30	Zor	Baklava yufkası, ceviz, şerbet	Baklava yufkaları arası ceviz konulur, şerbet dökülür.

🔍 Örnek Sorgular
"Malzemeleri un ve yumurta olan tatlılar nelerdir?"

"Hazırlaması 20 dakikadan kısa olan yemek tarifleri var mı?"

"Kolay ve pratik bir çorba önerir misin?"

"Merhaba" (selamlaşma yanıtı alırsınız)

👩‍🍳 Projenin Katkıları
Yemek yapmayı sevenlerin hızlıca aradıkları tariflere ulaşmalarını sağlar.

Kullanıcı dostu, doğal dil ile etkileşim imkanı sunar.

Tarif seçimini kolaylaştırarak mutfakta zaman kazandırır.

css
Kopyala
