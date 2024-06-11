import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_text(mp3_file_path):
    # MP3 dosyasını WAV formatına dönüştür
    audio = AudioSegment.from_mp3(mp3_file_path)
    wav_file_path = "lan.mp3"
    audio.export(wav_file_path, format="wav")

    # SpeechRecognition tanıyıcı nesnesi oluşturma
    recognizer = sr.Recognizer()

    # Ses dosyasını yükleyip metne dönüştürme
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            # Google Web Speech API kullanarak metne dönüştürme
            text = recognizer.recognize_google(audio_data, language="tr-TR")
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API sesi anlayamadı"
        except sr.RequestError as e:
            return f"Google Web Speech API hizmetine erişilemiyor; {e}"

# Örnek kullanım
mp3_file_path = "lan.mp3"
recognized_text = mp3_to_text(mp3_file_path)
print("Tanınan Metin: " + recognized_text)
