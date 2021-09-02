"""Scripts checks if a word exists in the HTML-text of a website.
Useful to detect if a website changes."""

import urllib.request
from win10toast import ToastNotifier


def website_word_checker():
    site = str(urllib.request.urlopen(url).read())
    if word in site:
        print(f"Word '{word}' found")
        notify()
    else:
        print(f"Word '{word}' not found")


def notify():
        toaster = ToastNotifier()
        toaster.show_toast(f"Word '{word}' found", " ")


if __name__ == '__main__':
    url = r"https://www.buchung.zhs-muenchen.de/angebote/aktueller_zeitraum_0/index.html"
    word = 'Wintersemester'
    website_word_checker()

