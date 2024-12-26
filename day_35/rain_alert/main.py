import requests
import os


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
owm_api_key = os.environ.get("OWM_API_KEY")
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot_chatID = os.environ.get("TELEGRAM_CHAT_ID")


weather_params = {
    "lat": 11.5782802263959,
    "lon": 104.90179009030645,
    "appid": owm_api_key,
    "cnt": 4,
}


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def fetch_weather_data():
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    return response.json()


def check_rain(data):
    for hour_data in data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            return True


try:
    weather_data = fetch_weather_data()
    if check_rain(weather_data):
        test = telegram_bot_sendtext("It's going to rain today. Remember to bring an ☔️")
        print(test)
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
