from pydub import AudioSegment
import speech_recognition as sr

# Inicializa el reconocedor de voz
r = sr.Recognizer()

# Carga el archivo mp3
audio = AudioSegment.from_mp3("audio.mp3")

# Guarda el archivo como wav
audio.export("audio.wav", format="wav")

# Abre el archivo de audio , tiene que ser wav
#probablemente transformar mp3 a wav
with sr.AudioFile('audio.wav') as source:
    audio = r.record(source)

# Usa el motor de reconocimiento de voz de Google
text = r.recognize_google(audio, show_all=True)

# Imprime el texto
print(text)
