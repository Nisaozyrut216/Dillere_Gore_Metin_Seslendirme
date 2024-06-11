from gtts import gTTS
import os
from os import path

def dosyaVarmi(dosya):
    return path.exists(dosya)
    

dosya = open("lonely.txt", encoding="utf-8")
yazi = dosya.read()
cikti = gTTS(text=yazi, lang='tr', slow=False)
if dosyaVarmi("ni.mp3"):
    print("seslendiriliyor....")
    os.system("ni.mp3")
else:
    print("Dosyanız oluşturuluyor")
cikti.save("ni.mp3")
print("seslendiriliyor....")
os.system("lonely.mp3")
dosya.close()