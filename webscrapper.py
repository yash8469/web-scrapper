from bs4 import BeautifulSoup
import requests
import time

session = requests.Session()
url = "https://www.aljazeera.com"  # we can change this to any site

r = session.get(url)
soup = BeautifulSoup(r.content, "html.parser")
soup.prettify()
# collecting text 
raw = soup.find_all(["h1", "h2", "h3"])

headlines = []
for tag in raw:
    text = tag.get_text(strip=True)
    if text and text not in headlines:  # avoid duplicates
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for headline in headlines:
        print(headline)
        f.write(headline + "\n")
        time.sleep(1)
