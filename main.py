import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

#optionals
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
cookies = [
    {"name": "NID", "value": "your_cookie_value_here", "domain": ".google.com"}
]

def addCookie(theDriver):
    for cookie in cookies:
            theDriver.add_cookie(cookie)
    theDriver.refresh()
    time.sleep(random.uniform(2, 4))
    

def uc_driver_setup():
    try:
        uc_driver = uc.Chrome()
        uc_driver.get("https://www.google.com")
        search_box = uc_driver.find_element(By.ID, "APjFqb")
        search_box.send_keys("practicetestautomation")
        search_box.submit()
        time.sleep(random.uniform(1, 3))
        website_link = uc_driver.find_element(By.XPATH, "/html/body/div[3]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/span/a")
        website_link.click()
        time.sleep(random.uniform(0, 2))
        practice_link = uc_driver.find_element(By.XPATH, "/html/body/div/div/header/div[3]/div[1]/div/div[2]/div/nav/ul/li[2]/a")
        practice_link.click()
        time.sleep(random.uniform(0, 2))
        practice_link = uc_driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/div[1]/div[1]/p/a")
        practice_link.click()
        username = uc_driver.find_element(By.ID, "username")
        username.send_keys("student")
        password = uc_driver.find_element(By.ID, "password")
        password.send_keys("Password123")
        btn_submit = uc_driver.find_element(By.ID, "submit")
        btn_submit.click()
        time.sleep(random.uniform(0, 2))
        
        uc_driver.close()
    except Exception as e:
        print(f"Error initializing : {e}")
        return
    finally:
        uc_driver.quit()

        
uc_driver_setup()