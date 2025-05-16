import sys
import os
from PyQt5.QtWidgets import QApplication
from views.auth_window.auth_login import AuthLoginWindow
from views.auth_window.auth_register import AuthRegisterWindow
from views.main_window.main import MainWindow
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class ApplicationManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = AuthLoginWindow(self)
        self.register_window = None
        self.main_window = None
        self.token = None
        self.websocket = None
        self.controller = None

    def show_login_window(self):
        self.login_window.show()
        if self.register_window:
            self.register_window.hide()
        if self.main_window:
            self.main_window.hide()

    def show_register_window(self):
        if not self.register_window:
            self.register_window = AuthRegisterWindow(self)
        self.register_window.show()
        self.login_window.hide()
        if self.main_window:
            self.main_window.hide()

    def show_main_window(self):
        if not self.main_window:
            self.main_window = MainWindow(self)
        self.main_window.show()    
        self.login_window.hide()
        if self.register_window:
            self.register_window.hide()

    def set_token(self, token):
        self.token = token
        print(f"Token stored in ApplicationManager: {self.token}")
    
    def get_token(self):
        return self.token

    def run(self):
        self.show_login_window()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app_manager = ApplicationManager()
    app_manager.run()
