from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout,
                             QPushButton, QComboBox, QLineEdit, QAction, QMenu)
from PyQt5.QtCore import (QSize,)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys
import os
from PyQt5.QtCore import Qt


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Storm Messenger")
        self.setGeometry(50, 40, 1850, 800)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #c5c6d1;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        central_widget.setLayout(self.main_layout)

        self.chats_widget = QWidget()
        self.chats_layout = QVBoxLayout()
        self.chats_layout.setContentsMargins(0, 0, 0, 0)
        self.chats_layout.setSpacing(0)

        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setSpacing(0)

        self.notification_widget = QWidget()
        self.notification_layout = QVBoxLayout()
        self.notification_layout.setContentsMargins(0, 0, 0, 0)
        self.notification_layout.setSpacing(0)

        self.main_layout.addWidget(self.chats_widget)
        self.chats_widget.setLayout(self.chats_layout)

        self.main_layout.addWidget(self.chat_widget)
        self.chat_widget.setLayout(self.chat_layout)

        self.main_layout.addWidget(self.notification_widget)
        self.notification_widget.setLayout(self.notification_layout)

        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 3)
        self.main_layout.setStretch(2, 1)

        #Это у нас чаты        
        self.icons_widget = QWidget()
        self.icons_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.icons_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.icons_widget)
        self.icons_widget.setLayout(self.icons_layout)
        self.chats_layout.setStretch(0, 0)

        self.x_widget =QWidget()
        self.x_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.x_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.x_widget)
        self.x_widget.setLayout(self.x_layout)
        self.chats_layout.setStretch(1, 0)

        self.about_widget = QWidget()
        self.about_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.about_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.about_widget)
        self.about_widget.setLayout(self.about_layout)
        self.chats_layout.setStretch(3, 2)

        self.search_widget = QWidget()
        self.search_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.search_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.search_widget)
        self.search_widget.setLayout(self.search_layout)
        self.chats_layout.setStretch(3, 0)

        self.message_widget = QWidget()
        self.message_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.message_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.message_widget)
        self.message_widget.setLayout(self.message_layout)
        self.chats_layout.setStretch(4, 1)

        #Иконки
        self.favourite_button = QPushButton()
        self.favourite_button.setFixedSize(50, 50)
        self.favourite_button.setStyleSheet("""
            QPushButton { background-color: #a0a3a1; color: white; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: #585c59; }
            QPushButton:pressed { background-color: #e80e17; }
            }
        """)
        self.favourite_button.setIcon(QIcon(resource_path("icons/bookmark-ribbon.png")))
        self.favourite_button.setIconSize(QSize(32, 32))
        self.icons_layout.addWidget(self.favourite_button)

        self.group_button = QPushButton()
        self.group_button.setFixedSize(50, 50)
        self.group_button.setStyleSheet("""
            QPushButton { background-color: #a0a3a1; color: white; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: #585c59; }
            QPushButton:pressed { background-color: #e80e17; }
            }
        """)
        self.group_button.setIcon(QIcon(resource_path("icons/team-28.png")))
        self.group_button.setIconSize(QSize(32, 32))
        self.icons_layout.addWidget(self.group_button)

        self.night_theme_button = QPushButton()
        self.night_theme_button.setFixedSize(50, 50)
        self.night_theme_button.setStyleSheet("""
            QPushButton { background-color: #a0a3a1; color: white; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: #585c59; }
            QPushButton:pressed { background-color: #e80e17; }
            }
        """)
        self.night_theme_button.setIcon(QIcon(resource_path("icons/evening-icon.svg")))
        self.night_theme_button.setIconSize(QSize(32, 32))
        self.icons_layout.addWidget(self.night_theme_button)

        self.customization_button = QPushButton()
        self.customization_button.setFixedSize(50, 50)
        self.customization_button.setStyleSheet("""
            QPushButton { background-color: #a0a3a1; color: white; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: #585c59; }
            QPushButton:pressed { background-color: #e80e17; }
            }
        """)
        self.customization_button.setIcon(QIcon(resource_path("icons/597182.png")))
        self.customization_button.setIconSize(QSize(32, 32))
        self.icons_layout.addWidget(self.customization_button)

        #Кнопка добавить
        self.x_label = QLabel("Чаты")
        self.x_label.setStyleSheet("""
            QLabel {
                color: #08090a;
                font-size: 30px;
                font-family: 'Arial';
                font-weight: bold;
                padding-left: 5px;
            }
        """)
        self.x_layout.addWidget(self.x_label)

        self.x_box = QPushButton()
        self.x_box.setFixedSize(45, 45)
        self.x_box.setStyleSheet("""
            QPushButton {
                background-color: #781778;
                color: white;
                border-radius: 22px;  
                font-size: 14px;
                padding: 0px;
            }
            QPushButton::drop-down {
                border: none;
                width: 0px;
            }
            QPushButton::down-arrow {
                image: none;
            }
        """)
        self.x_box.setIcon(QIcon(resource_path("icons/plus-math.png")))
        self.x_layout.addWidget(self.x_box)

        #Прочее
        self.all_button = QPushButton("Все")
        self.all_button.setStyleSheet("""
            QPushButton { background-color: white; color: #736d73; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: white; }
            QPushButton:pressed { background-color: white; }
            }
        """)
        self.about_layout.addWidget(self.all_button)

        self.private_button = QPushButton("Приватные")
        self.private_button.setStyleSheet("""
            QPushButton { background-color: white; color: #736d73; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: white; }
            QPushButton:pressed { background-color: white; }
            }
        """)
        self.about_layout.addWidget(self.private_button)

        self.common_button = QPushButton("Общие")
        self.common_button.setStyleSheet("""
            QPushButton { background-color: white; color: #736d73; border-radius: 10px; padding: 10px; font-size: 18px; border: none; }
            QPushButton:hover { background-color: white; }
            QPushButton:pressed { background-color: white; }
            }
        """)
        self.about_layout.addWidget(self.common_button)

        self.more_box = QComboBox()
        self.more_box.addItem("Еще ▼")
        self.more_box.setFixedHeight(50)  
        self.more_box.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: #736d73;
                border-radius: 10px;
                padding: 10px;
                font-size: 18px;
                border: none;
            }
            QComboBox::drop-down {
                border: none;
                width: 0px; /* скрываем стрелку */
            }
            QComboBox::down-arrow {
                image: none;
            }
        """)
        self.about_layout.addWidget(self.more_box)

        #Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск людей и каналов...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 15px;
                font-size: 18px;
                color: #333333;
            }
        """)
        search_icon = QIcon(resource_path("icons/icons8-поиск.svg"))  
        search_action = QAction(search_icon, "", self.search_input)
        self.search_input.addAction(search_action, QLineEdit.LeadingPosition)
        self.search_layout.addWidget(self.search_input)

        #Чат
        self.message_label = QLabel()
        self.message_layout.addWidget(self.message_label)

        #Это у нас чат
        self.phone_widget = QWidget()
        self.phone_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.phone_layout = QHBoxLayout()
        self.chat_layout.addWidget(self.phone_widget)
        self.phone_widget.setLayout(self.phone_layout)
        self.chat_layout.setStretch(0, 0)

        self.info_widget = QWidget()
        self.info_widget.setStyleSheet("""
            QWidget {
                background-color: #c2bfb8;
            }
        """)
        self.info_layout = QHBoxLayout()
        self.chat_layout.addWidget(self.info_widget)
        self.info_widget.setLayout(self.info_layout)
        self.chat_layout.setStretch(0, 0)

        self.name_button = QPushButton("Маша Машаева")
        self.name_button.setStyleSheet("""
            QPushButton {
                color: #08090a;
                font-size: 30px;
                font-family: 'Arial';
                font-weight: bold;
                padding-left: 15px;
            }
        """)
        self.phone_layout.addWidget(self.name_button)

        #Это у нас уведомление
        self.notification_label = QLabel("Здесь будут уведомление")
        self.notification_layout.addWidget(self.notification_label)

if __name__ == "__main__":
    app_manager = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app_manager.exec_())
