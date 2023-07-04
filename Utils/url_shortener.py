import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

# Usage example:
# Shortens a long URL
long_url = 'https://www.example.com/long/url/here'
short_url = shorten_url(long_url)
print(short_url)
