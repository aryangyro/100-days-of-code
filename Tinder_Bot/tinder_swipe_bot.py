import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROFILE_PATH = "/Users/aryanpanwar/Library/Application Support/Google/Chrome"

options = Options()
options.add_argument(f"--user-data-dir={PROFILE_PATH}")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Step 1: Open homepage
driver.get("https://tinder.com")

# Step 2: Wait until Tinder app UI loads (main app container)
wait = WebDriverWait(driver, 40)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

print("App initialized")

# Step 3: Now go to recs page
driver.get("https://tinder.com/app/recs")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
print("Recs page loaded")

time.sleep(30)
