import requests
from datetime import datetime

# NutritionIX
APP_ID = "d78dcd60"
API_KEY = "1c5f2b1a046b8ef81c40f03e7eb746b2	"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
NATURAL_LANG = "/v2/natural/exercise"
NL_ENDPOINT = f"{HOST_DOMAIN}{NATURAL_LANG}"

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
# print(data)
# print(exercise)
# print(duration)




# Sheety
SHEETY_ENDPOINT = "https://api.sheety.co/e938eee05710f2891def63457d60664d/myWorkouts/workouts"

# sheety_response = requests.get(url=SHEETY_ENDPOINT)
# print(sheety_response.text)



today = datetime.now()
logdate = today.strftime("%d/%m/%Y")
logtime = today.strftime("%H:%M:%S")

# print(today)
# print(logdate)
# print(logtime)

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