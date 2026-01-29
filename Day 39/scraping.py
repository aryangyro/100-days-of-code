from bs4 import BeautifulSoup
import requests
import re

web = "https://www.passportsandpreemies.com/places-to-visit-in-europe/"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
})

response = session.get(web)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

def srt(filename):
    rows = set()

    # Read file
    with open(filename, "r") as file:
        header = file.readline()

        for line in file:
            parts = line.strip().split(",")

            # Skip broken lines
            if len(parts) != 2:
                continue

            city, country = parts
            rows.add((country.strip(), city.strip()))

    # Sort by country, then city
    rows = sorted(rows,key=lambda x: (x[0].lower(), x[1].lower()))

    # Write back grouped data
    with open(filename, "w") as file:
        for country, city in rows:
            file.write(f"{city},{country}\n")




cities = []

for h2 in soup.find_all("h2"):
    ans = h2.get_text(strip=True)

    if ans == "FAQ":
        continue

    clean_city = re.sub(r'^\d+[\.\-\)]\s*', '', ans)
    cities.append(clean_city)


try:
    with open("style.csv", "r") as file:
        existing = set(line.strip() for line in file)
except FileNotFoundError:
    existing = set()


with open("style.csv", "a") as file:
    for city in cities:
        if city not in existing:
            file.write(city + "\n")

srt("style.csv")
