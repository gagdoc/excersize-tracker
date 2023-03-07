import requests
from datetime import datetime
today = datetime.today().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%X")

time = 14
exercise_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
google_sheet_post_endpoint = "https://api.sheety.co/a65a5261a2264fc12b066bf2426cd8bc/myWorkouts/workouts"
GENDER = "male"
WEIGTH = 75
HEIGTH = 170
AGE = 48
ASK_TODAY_EXE = input("오늘 무슨 운동 했어? ")

APP_ID = "8c39983d"
API_KEY = "58b12cdd16933e75a30d4fd69e576c1e"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "gender": GENDER,
    "query": ASK_TODAY_EXE,
    "weight_kg": WEIGTH,
    "height_cm": HEIGTH,
    "age": AGE
}

response = requests.post(exercise_end_point, headers=headers, json=params)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
            }
        }
    sheet_response = requests.post(google_sheet_post_endpoint, json=sheet_inputs)
    print(sheet_inputs)



