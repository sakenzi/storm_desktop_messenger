from PyQt5.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, 
                             QLabel, QSizePolicy, QLineEdit,)
from PyQt5.QtCore import (QPersistentModelIndex)
from PyQt5.QtGui import (QPixmap,)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from styles.auth_login_components import Styles
from icons.icon import ICONS
from controllers.auth_controller import AuthWindowController


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_layouts()
        self._wallpaper_panel()
        self._setup_auth_login_panel()
        self.controller = AuthWindowController()

    def _setup_window(self):
        self.setWindowTitle("Аутентификация")
        self.setGeometry(50, 40, 1850, 800)
        self.setStyleSheet(Styles['auth_window'])

    def _setup_layouts(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        central_widget.setLayout(self.main_layout)

        self.wallpaper_widget = QWidget()
        self.wallpaper_layout = QVBoxLayout()
        self.wallpaper_layout.setContentsMargins(0, 0, 0, 0)
        self.wallpaper_layout.setSpacing(0)
        self.wallpaper_widget.setLayout(self.wallpaper_layout)

        self.auth_login_widget = QWidget()
        self.auth_login_layout = QVBoxLayout()
        self.auth_login_layout.setContentsMargins(0, 0, 0, 0)
        self.auth_login_layout.setSpacing(0)
        self.auth_login_widget.setLayout(self.auth_login_layout)

        self.main_layout.addWidget(self.wallpaper_widget)
        self.main_layout.addWidget(self.auth_login_widget)

        # self.main_layout.setStretch(0, 1)
        # self.main_layout.setStretch(1, 0)

    def _wallpaper_panel(self):
        wallpaper_label = QLabel()
        pixmap = QPixmap("photo/chernila_zhidkost_kraska_182805_3840x2400.jpg")
        wallpaper_label.setPixmap(pixmap)
        wallpaper_label.setScaledContents(True)
        wallpaper_label.setFixedSize(1200, 1000)
        self.wallpaper_layout.addWidget(wallpaper_label)

    def _setup_auth_login_panel(self):
        self._create_emblem_panel()
        self._welcome_speech()
        self._username_label()
        self._username_input()
        self._fullname_label()
        self._fullname_input()
        self._password_label()
        self._password_input()
        self._sign_up()

    def _create_emblem_panel(self):
        emblem_widget = QWidget()
        emblem_widget.setStyleSheet(Styles['emblem_widget'])
        emblem_layout = QHBoxLayout()
        emblem_widget.setLayout(emblem_layout)
        self.auth_login_layout.addWidget(emblem_widget)

        emblem_label = QLabel()
        pixmap = QPixmap(ICONS['emblem'])
        emblem_label.setPixmap(pixmap)
        emblem_label.setScaledContents(True)
        emblem_label.setFixedSize(50, 50)
        emblem_layout.addWidget(emblem_label)

        text_label = QLabel("Storm Messenger")
        text_label.setStyleSheet(Styles['emblem_label'])
        emblem_layout.addWidget(text_label)

        self.auth_login_layout.setStretch(0, 0)

    def _welcome_speech(self):
        speech_widget = QWidget()
        speech_widget.setStyleSheet(Styles['emblem_widget'])
        speech_layout = QHBoxLayout()
        speech_widget.setLayout(speech_layout)
        self.auth_login_layout.addWidget(speech_widget)

        speech_label = QLabel("Nice to see you again")
        speech_label.setStyleSheet(Styles['speech_label'])
        speech_layout.addWidget(speech_label)

        self.auth_login_layout.setStretch(1, 1)
    
    def _username_label(self):
        username_widget = QWidget()
        username_widget.setStyleSheet(Styles['emblem_widget'])
        username_layout = QHBoxLayout()
        username_widget.setLayout(username_layout)
        self.auth_login_layout.addWidget(username_widget)

        username_label = QLabel("Username")
        username_label.setStyleSheet(Styles['login_label'])
        username_layout.addWidget(username_label)

        self.auth_login_layout.setStretch(2, 0)

    def _username_input(self):
        username_input_widget = QWidget()
        username_input_widget.setStyleSheet(Styles['emblem_widget'])
        username_input_layout = QHBoxLayout()
        username_input_widget.setLayout(username_input_layout)
        self.auth_login_layout.addWidget(username_input_widget)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username ")
        self.username_input.setStyleSheet(Styles['login_input'])
        username_input_layout.addWidget(self.username_input)

        self.auth_login_layout.setStretch(3, 0)

    def _fullname_label(self):
        fullname_widget = QWidget()
        fullname_widget.setStyleSheet(Styles['emblem_widget'])
        fullname_layout = QHBoxLayout()
        fullname_widget.setLayout(fullname_layout)
        self.auth_login_layout.addWidget(fullname_widget)

        fullname_label = QLabel("Full name")
        fullname_label.setStyleSheet(Styles['login_label'])
        fullname_layout.addWidget(fullname_label)

        self.auth_login_layout.setStretch(4, 0)

    def _fullname_input(self):
        fullname_input_widget = QWidget()
        fullname_input_widget.setStyleSheet(Styles['emblem_widget'])
        fullname_input_layout = QHBoxLayout()
        fullname_input_widget.setLayout(fullname_input_layout)
        self.auth_login_layout.addWidget(fullname_input_widget)

        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Full name")
        self.fullname_input.setStyleSheet(Styles['login_input'])
        fullname_input_layout.addWidget(self.fullname_input)

        self.auth_login_layout.setStretch(5, 0)

    def _password_label(self):
        password_widget = QWidget()
        password_widget.setStyleSheet(Styles['emblem_widget'])
        password_layout = QHBoxLayout()
        password_widget.setLayout(password_layout)
        self.auth_login_layout.addWidget(password_widget)

        password_label = QLabel("Password")
        password_label.setStyleSheet(Styles['login_label'])
        password_layout.addWidget(password_label)

        self.auth_login_layout.setStretch(6, 0)

    def _password_input(self):
        password_input_widget = QWidget()
        password_input_widget.setStyleSheet(Styles['emblem_widget'])
        password_input_layout = QHBoxLayout()
        password_input_widget.setLayout(password_input_layout)
        self.auth_login_layout.addWidget(password_input_widget)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setStyleSheet(Styles['login_input'])
        password_input_layout.addWidget(self.password_input)

        self.auth_login_layout.setStretch(7, 0)

    def _sign_up(self):
        sign_up_widget = QWidget()
        sign_up_widget.setStyleSheet(Styles['emblem_widget'])
        sign_up_layout = QHBoxLayout()
        sign_up_widget.setLayout(sign_up_layout)
        self.auth_login_layout.addWidget(sign_up_widget)

        sign_up_button = QPushButton("Sign Up")
        sign_up_button.setStyleSheet(Styles['sign_in_button'])
        sign_up_layout.addWidget(sign_up_button)

        self.auth_login_layout.setStretch(8, 1)
    
        sign_up_button.clicked.connect(self.on_register_button_clicked)
        
    def on_register_button_clicked(self):
        success, message = self.controller.handle_register(
            self.username_input.text(),
            self.fullname_input.text(),
            self.password_input.text()
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
