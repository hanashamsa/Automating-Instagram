import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")


chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

# Step 1: Open Instagram
driver.get("https://www.instagram.com/")

# Step 2: Accept cookies
try:
    allow_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Allow all cookies']")))
    allow_cookies.click()
except:
    print("Cookies banner not found.")

# Step 3: Login process
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.clear()
username_field.send_keys(USERNAME)

password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.clear()
password_field.send_keys(PASSWORD)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Step 4: Dismiss "Save Login Info"
try:
    not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    not_now_btn.click()
except:
    print("No 'Save Login Info' popup found.")

# Step 5: Dismiss "Turn on Notifications"
try:
    notif_not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    notif_not_now.click()
except:
    print("No 'Turn on Notifications' popup found.")

# Step 6: Like first post
try:
    first_like_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//article//section//span/button)[1]")))
    first_like_btn.click()
    print("First post liked ")
except:
    print("First post not found or already liked.")

time.sleep(3)
driver.quit()
