import requests
import smtplib

#Alert me for the rain
MY_LONG = -79.644119
MY_LAT = 43.589046
API_KEY = "yourapi key"
OPEN_ENDPOINT= 'https://api.openweathermap.org/data/3.0/onecall'
MY_EMAIL = "email@gmail.com"
password="dwadawca"

parameters= {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
}

response = requests.get(url = OPEN_ENDPOINT, params= parameters)
response.raise_for_status()
data = response.json()



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login (user= MY_EMAIL, password = password)
    connection.sendmail (from_addr=MY_EMAIL, to_addrs="email@gmail.com"
    msg = f"Subject: Today's Weather \n\n {data}"
    )
