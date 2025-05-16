from model.models import AuthLoginData, AuthRegisterData
from api_handlers.auth import register as register_request, login as login_request
import json


class AuthWindowController:
    def __init__(self, window=None):
        self.window = window
        self.token = None

    def handle_login(self, username, password):
        if not username or not password:
            print("Поля не должно быть пустым")
            return False, "Поля не должны быть пустыми"
        
        data = AuthLoginData(username, password).to_dict()
        response = login_request(data)

        if response:
            json_response = response.json()
            if "access_token" in json_response:
                self.token = json_response["access_token"]
                print(f"Токен: {self.token}")

        if response is not None:
            if response.status_code == 200:
                print("Успешный вход")
                print(response.json())
                return True, "Успешный вход"
            else:
                print("Ошибка входа")
                return False, f"Ошибка входа: {response.status_code}"
        else:
            return False, "Ошибка сети или сервера"

    def handle_register(self, username, fullname, password):
        if not username or not fullname or not password:
            print("Поля не должно быть пустым")
            return False, "Поля не должны быть пустыми"
        
        data = AuthRegisterData(username, fullname, password).to_dict()
        response = register_request(data)

        if response:
            json_response = response.json()
            if "access_token" in json_response:
                self.token = json_response["access_token"]
                print(f"Токен: {self.token}")

        if response is not None:
            if response.status_code == 200:
                print("Успешная регистрация")
                print(response.json())
                return True, "успешная регистрация"
            else:
                print("Ошибка регистраций")
                return False, f"Ошибка регистраций: {response.status_code}"
        else:
            return False, "Ошибка сети или сервера"
        
    def get_token(self):
        return self.token
