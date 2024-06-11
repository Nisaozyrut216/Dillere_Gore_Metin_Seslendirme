from gtts import gTTS
import os
from os import path

def dosyaVarmi(dosya):
    return path.exists(dosya)

def seslendir(text, dil='tr'):
    # Ses dosyasını oluştur
    cikti = gTTS(text=text, lang=dil, slow=False)
    # Ses dosyasını kaydet
    cikti.save("ses.mp3")
    # Ses dosyasını oynat
    os.system("start ses.mp3")

dosya_adı = "rusca.txt"

# Dosya varsa
if dosyaVarmi(dosya_adı):
    # Dosyayı aç ve içeriğini oku
    with open(dosya_adı, encoding="utf-8") as dosya:
        yazi = dosya.read()
        # Seslendirme yap
        seslendir(yazi, dil='ru')  # Türkçe olarak seslendir
else:
    print("Belirtilen dosya bulunamadı.")
