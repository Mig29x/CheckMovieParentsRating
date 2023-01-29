import feedparser
import urllib.request

rss_url = 'https://nihongoconteppeiz.com/feed/podcast/' # Reemplaza por la URL del RSS del podcast
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    audio_url = entry.enclosures[0].url 
    print(audio_url) # Imprime la URL del audio
    if audio_url.endswith('.mp3'):
        urllib.request.urlretrieve(audio_url, 'audio.mp3')
        break
