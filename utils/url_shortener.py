"""
Title: URL shortener
Description: Shortens a given URL using pyshorteners
Author: Benji377
Created: 04.07.2023
Last Updated: 04.07.2023

Usage:
    No parameters

Dependencies:
    - pyshorteners
    (Install with: pip install pyshorteners)

Notes:
    - This script is standalone and does not require other files from the repo.
    - Adjust any parameters or constants at the top of the script as needed.
"""


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
