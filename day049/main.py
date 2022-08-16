from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PASSWORD = PASSWORD
EMAIL = EMAIL

chrome_driver_path = YOUR CHROME DRIVER
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2917980952&f_AL=true&f_E=2&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States")


sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

email_link = driver.find_element(By.NAME, "session_key")
email_link.send_keys(EMAIL)

password_link = driver.find_element(By.NAME, "session_password")
password_link.send_keys(PASSWORD)
password_link.send_keys(Keys.ENTER)



job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
listing_no = len(job_listings)


for index in range(listing_no):
    job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    job = job_listings[index]
    job.click()
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save.click()



