from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = YOUR CROME DRIVER
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
cookies_per_sec = driver.find_element(By.ID, "cps")
money = driver.find_element(By.ID, "money")
timeout = time.time() + 60 * 1  # 5 minutes from now
five_sec = time.time() + 5


while True:
    cookie.click()
    if time.time() > five_sec:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for product in store[::-1]:
            if product.get_attribute("class") != "grayed":
                try:
                    product_id = product.get_attribute("id")
                    driver.find_element(By.ID, product_id).click()
                except StaleElementReferenceException as e:
                    print(f"Exception found: {e}")
                    pass

        timeout = time.time() + 5

    elif time.time() > timeout:
        print(cookies_per_sec.text)
        break
