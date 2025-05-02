import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OWM_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Request weather data
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4  # check next 12 hours (3h x 4)
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check for rain in the forecast
rain_times = [
    hour_data["dt_txt"]
    for hour_data in weather_data["list"]
    if int(hour_data["weather"][0]["id"]) < 700
]


# Send Telegram message if rain is expected
def telegram_bot_sendtext(bot_message):
    send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "parse_mode": "Markdown",
        "text": bot_message
    }
    bot_response = requests.get(send_url, params=params)
    return bot_response.json()


if rain_times:
    message = "🌧 *Rain Alert!*\nRain expected at:\n" + "\n".join(rain_times) + "\n\nBring an umbrella ☔"
    telegram_bot_sendtext(message)
