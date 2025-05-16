from dotenv import load_dotenv
import requests
import os


load_dotenv()

api = os.getenv("API_BASE_URL")

def register(data):
    url = f"{api}/v1/auth/user/register"
    print(data)
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Қате {e}")


def login(data):
    url = f"{api}/v1/authuser/login"
    print(data)
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Қате {e}")