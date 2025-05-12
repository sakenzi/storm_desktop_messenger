from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout,
                             QPushButton, )
from PyQt5.QtCore import (QSize,)
from PyQt5.QtGui import (QIcon, )
import sys
import os


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
                background-color: #fafcfb;
            }
        """)
        self.icons_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.icons_widget)
        self.icons_widget.setLayout(self.icons_layout)
        self.chats_layout.setStretch(0, 0)

        self.message_widget = QWidget()
        self.message_widget.setStyleSheet("""
            QWidget {
                background-color: #fafcfb;
            }
        """)
        self.message_layout = QHBoxLayout()
        self.chats_layout.addWidget(self.message_widget)
        self.message_widget.setLayout(self.message_layout)
        self.chats_layout.setStretch(1, 2)

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

        #Это у нас чат
        self.chat_label = QLabel("Здесь будут чат")
        self.chat_layout.addWidget(self.chat_label)

        #Это у нас уведомление
        self.notification_label = QLabel("Здесь будут уведомление")
        self.notification_layout.addWidget(self.notification_label)

if __name__ == "__main__":
    app_manager = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app_manager.exec_())
