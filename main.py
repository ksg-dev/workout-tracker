import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv(".env")
# NutritionIX
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
NL_ENDPOINT = os.getenv("NL_ENDPOINT")

# Sheety
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


user_input = input("Enter your exercise: ")

exercise_config = {
    "query": user_input,
}

response = requests.post(url=NL_ENDPOINT, json=exercise_config, headers=headers)
data = response.json()

exercise = data["exercises"][0]["name"].title()
duration = int(data["exercises"][0]["duration_min"])
calories = int(data["exercises"][0]["nf_calories"])

today = datetime.now()
logdate = today.strftime("%d/%m/%Y")
logtime = today.strftime("%H:%M:%S")

new_row = {
    "workout": {
        "date": logdate,
        "time": logtime,
        "exercise": exercise,
        "duration": duration,
        'calories': calories,
    }
}

add_row = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=headers)