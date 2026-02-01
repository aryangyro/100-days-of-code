import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdl6z03H7n5tnOCJM6INQ8EkNcRVVeNxI2JWSjnk6KGKr_xTw/viewform")

for item in data:
    
    # 1. Give the page 2 seconds to load so elements exist
    time.sleep(2)

    if item["price"] < 2500:
    
        address_input = driver.find_element(By.XPATH, 
            '(//input[@type="text"])[2]')
        address_input.send_keys(item["address"])
        
        # 3. Find Price Input
        # This looks for the second text input on the page
        price_input = driver.find_element(By.XPATH, 
            '(//input[@type="text"])[1]')
        price_input.send_keys(str(item["price"])) # str() ensures no errors with numbers
        
        # 4. Find Link Input
        # This looks for the third text input on the page
        link_input = driver.find_element(By.XPATH, 
            '(//input[@type="text"])[3]')
        link_input.send_keys(item["link"])

        submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]")
        submit_button.click()
        
        time.sleep(2) # Wait for submit to finish

        next_button = driver.find_element(By.LINK_TEXT, "Submit another response")
        next_button.click()







    








