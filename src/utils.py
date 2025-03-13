from typing import Any
import requests
import dotenv
import os

dotenv.load_dotenv()

def get_weather_details(latitude: float, longitude: float) -> dict[str, Any] | str:

    API_KEY = os.getenv("API_KEY")
    print("API_KEY", API_KEY)

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            return response.json()
        
        print(response.reason)
        return response.reason

    except Exception as e:
        print(e)
        return "Something went wrong!2"

