import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

API_KEY = #your key
MY_LAT = #your lat
MY_LONG = #your long

account_sid = #your account id
auth_token = #your auth_token




parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for num in range(0, 11):
    weather_id = weather_data["hourly"][num]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
             body="It's going to rain today, Bring an umbrella!",
             from_='number to send from',
             to='your number'
     )

    print(message.status)
