import requests

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

print(response.text)