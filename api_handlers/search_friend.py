import requests
from dotenv import load_dotenv
import os


load_dotenv()

api = os.getenv("API_BASE_URL")

def get_search_user(username):
    response = requests.get(f"{api}/v1/user_search/search/users",params={"username": username})
    return response