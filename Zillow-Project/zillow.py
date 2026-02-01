import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver

url = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url=url,headers=headers)

html = response.text

srch = BeautifulSoup(html,"html.parser")

def clean_price(text):
    match = re.search(r"\d[\d,]*", text)
    return int(match.group().replace(",", "")) if match else None

prices = srch.find_all("span",attrs={"data-test" : "property-card-price"})
adress = srch.find_all("address",attrs={"data-test" : "property-card-addr"})
links = srch.find_all("a",attrs={"data-test":"property-card-link"})

data = [
    {
        "price": clean_price(p.text),
        "address": a.text.strip(),
        "link": l.get("href")
    }
    for p, a, l in zip(prices, adress, links)
]

with open("properties.json", "w") as file:
    json.dump(data, file, indent=4)


driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdl6z03H7n5tnOCJM6INQ8EkNcRVVeNxI2JWSjnk6KGKr_xTw/viewform")








    








