from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PASSWORD = PASSWORD
EMAIL = EMAIL

chrome_driver_path = "YOUR CHROME DRIVER
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://tinder.com/")
main_page = driver.current_window_handle

action = ActionChains(driver)

login = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/main/div['
                                       '1]/div/div/div/div/header/div/div[2]/div[2]/a').click()


driver.implicitly_wait(5) # seconds

accept_cookies = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[2]/div/div/div[1]/button').click()

driver.maximize_window()

driver.implicitly_wait(5) # seconds

google_sign_in = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
driver.implicitly_wait(1) # seconds
google_sign_in.send_keys(Keys.ENTER)
driver.implicitly_wait(3) # seconds
action.double_click(google_sign_in).perform()

l = driver.find_element(By.TAG_NAME, "button")
l.send_keys(Keys.ENTER)


driver.implicitly_wait(30)

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)

email_sign_in = driver.find_element(By.TAG_NAME, 'input')
driver.implicitly_wait(3)
email_sign_in.send_keys(EMAIL)
driver.implicitly_wait(3)
email_sign_in.send_keys(Keys.ENTER)
