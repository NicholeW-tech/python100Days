import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B0193V3DJ6"
MY_EMAIL = "test.fur@gmail.com"
MY_PASSWORD = "test"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 "
              "Safari/537.36 Edg/98.0.1108.43 ",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")

# print(soup.prettify())
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price_total = float(f"{price_whole}{price_fraction}")

target_price = 447.00

if price_total < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Price Drop for Nordic Track Treadmill!\n\nThe NordicTrack Treadmill is ${price_total}\n{URL} ")
