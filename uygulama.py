import streamlit as st
from gtts import gTTS
import os
from os import path

def dosya_var_mi(dosya):
    return path.exists(dosya)

def seslendir(text, dil='tr'):
    # Ses dosyasını oluştur
    cikti = gTTS(text=text, lang=dil, slow=False)
    # Ses dosyasını kaydet
    cikti.save("ses.mp3")
    # Ses dosyasını oynat
    os.system("start ses.mp3")

# Dil seçenekleri
dil_secenekleri = {
    "Türkçe": "tr",
    "İngilizce": "en",
    "İspanyolca": "es",
    "Fransızca": "fr",
    "Almanca": "de",
    "Rusça": "ru",
    "Çince": "zh-CN",
    "Japonca": "ja",
    "İtalyanca": "it",
    "Arapça": "ar"
}

# Streamlit arayüzü
st.title("Metni Sese Dönüştürme Uygulaması")

# Dil seçeneği
secilen_dil = st.selectbox("Lütfen bir dil seçin:", list(dil_secenekleri.keys()))

# Metin dosyası yükleme
dosya = st.file_uploader("Lütfen bir metin dosyası yükleyin:", type=["txt"])

# Seslendirme işlemi
if dosya is not None:
    if dosya_var_mi(dosya.name):
        yazi = dosya.read().decode("utf-8")
        st.write("Metin dosyası başarıyla yüklendi.")
        st.write("Metin:")
        st.write(yazi)
        
        if st.button("Metni Sese Dönüştür"):
            dil_kodu = dil_secenekleri[secilen_dil]
            seslendir(yazi, dil=dil_kodu)
            st.write("Metin başarıyla sese dönüştürüldü. İşitme cihazınızı kontrol edin.")
    else:
        st.error("Belirtilen dosya bulunamadı.")
