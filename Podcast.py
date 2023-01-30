import feedparser
import urllib.request
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr

# Carga el archivo MP3
audio = AudioSegment.from_file("audio.mp3", format="mp3")

# Convierte el archivo a formato WAV
audio.export("audio.wav", format="wav")

# Crea chunks de audio
chunks = make_chunks(audio, chunk_length_ms=5000)

# Instancia de reconocimiento de voz
r = sr.Recognizer()

# Procesa cada chunk
for i, chunk in enumerate(chunks):
    # Guarda el chunk a un archivo temporal
    chunk.export("chunk{}.wav".format(i), format="wav")
    with sr.AudioFile("chunk{}.wav".format(i)) as source:
        audio = r.record(source)
    # Reconoce el texto en el chunk
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("No se pudo reconocer el texto en el chunk {}".format(i))
    except sr.RequestError as e:
        print("Error al reconocer el texto en el chunk {}: {}".format(i, e))


rss_url = 'https://nihongoconteppeiz.com/feed/podcast/' # Reemplaza por la URL del RSS del podcast
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    audio_url = entry.enclosures[0].url 
    print(audio_url) # Imprime la URL del audio
    if audio_url.endswith('.mp3'):
        urllib.request.urlretrieve(audio_url, 'audio.mp3')
        break
