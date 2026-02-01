import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PROFILE_PATH = "/Users/aryanpanwar/Library/Application Support/Google/Chrome"

options = Options()

prefs = {
    "profile.default_content_setting_values.geolocation": 1, # 1 = Allow, 2 = Block
    "profile.default_content_setting_values.notifications": 1 
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--user-data-dir=/Users/aryanpanwar/Desktop/TinderBot") 
options.add_argument("--profile-directory=Default")


options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.get("https://tinder.com/app/recs")

while True:
    try:
        # Look for the button with the label 'Like'
        like_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="LIKE" or text()="Like"]]')))        
        like_button.click()
        print("Liked!")
        time.sleep(2) # Sleep to avoid looking like a bot
        
    except Exception as e:
        # If the click fails, try hitting 'Escape' to close any pop-ups
        print("Pop-up detected or button missing. Trying to dismiss...")
        from selenium.webdriver.common.keys import Keys
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(2)




time.sleep(300)
driver.quit()