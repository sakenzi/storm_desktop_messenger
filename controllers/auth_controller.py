from model.models import AuthLoginData, AuthRegisterData
from api_handlers.auth import register as register_request, login as login_request
import json


class AuthWindowController:
    def __init__(self, ui):
        self.ui = ui

    def handle_login(self):
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()

        if not username or not password:
            print("Поля не должно быть пустым")
            return 
        
        data = AuthLoginData(username=username, password=password).to_dict()
        response = login_request(data)

        if response and response.status_code == 200:
            print("Успешный вход")
            print(response.json())
        else:
            print("Ошибка")

    def handle_register(self):
        username = self.ui.username_input.text().strip()
        fullname = self.ui.fullname_input.text().strip()
        password = self.ui.password_input.text().strip()

        if not username or not fullname or not password:
            print("Поля не должно быть пустым")
            return
        
        data = AuthRegisterData(username=username, fullname=fullname, password=password).to_dict()
        response = register_request(data)

        if response and response.status_code == 200:
            print("Успешная регистрация")
            print(response.json())
        else:
            print("Ошибка регистраций")
