from api_handlers.search_friend import get_search_user
from model.models import SearchUser
import json


class SearchUserController:
    def __init__(self):
        pass

    def search_users(self, username: str) -> list[SearchUser]:
        response = get_search_user(username)
        if response.status_code == 200:
            users_json = response.json()
            print(users_json)
            users = [SearchUser(**user) for user in users_json]
            return users
        else:
            print("Ошибка при поиске:", response.status_code, response.text)
            return []