import feedparser

rss_url = 'https://nihongoconteppeiz.com/feed/podcast/' # Reemplaza por la URL del RSS del podcast
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(entry.enclosures[0].url) # Imprime la URL del audio
