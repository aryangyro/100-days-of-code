from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/cookieclicker/")  

sleep(3)

cookie_accept = driver.find_element(By.XPATH,'/html/body/div[1]/div/a[1]')
cookie_accept.send_keys(Keys.ENTER)



language_select = driver.find_element(by=By.ID, value="langSelect-EN")

try:
    language_select.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("can't do")
    








