import sys
import os
from PyQt5.QtWidgets import QApplication
from views.auth_window.auth_login import AuthLoginWindow
from views.auth_window.auth_register import AuthRegisterWindow
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class ApplicationManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = AuthLoginWindow(self)
        self.register_window = None
        self.token = None
        self.websocket = None
        self.controller = None

    def show_login_window(self):
        self.login_window.show()

    def run(self):
        self.show_login_window()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app_manager = ApplicationManager()
    app_manager.run()
