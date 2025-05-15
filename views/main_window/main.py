from PyQt5.QtWidgets import (
    QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLineEdit, QAction, QLabel, QMenu
)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from styles.main_window_components import Styles
from icons.icon import ICONS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_layouts()
        self._setup_chats_panel()
        self._setup_chat_panel()
        self._setup_notification_panel()

    def _setup_window(self):
        """Настройка основного окна приложения."""
        self.setWindowTitle("Storm Messenger")
        self.setGeometry(50, 40, 1850, 800)
        self.setStyleSheet(Styles['main_window'])

    def _setup_layouts(self):
        """Создание основов приложения."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        central_widget.setLayout(self.main_layout)

        # Панель чатов
        self.chats_widget = QWidget()
        self.chats_layout = QVBoxLayout()
        self.chats_layout.setContentsMargins(0, 0, 0, 0)
        self.chats_layout.setSpacing(0)
        self.chats_widget.setLayout(self.chats_layout)

        # Панель сообщений
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setSpacing(0)
        self.chat_widget.setLayout(self.chat_layout)

        # Панель уведомлений
        self.notification_widget = QWidget()
        self.notification_layout = QVBoxLayout()
        self.notification_layout.setContentsMargins(0, 0, 0, 0)
        self.notification_layout.setSpacing(0)
        self.notification_widget.setLayout(self.notification_layout)

        # Добавление виджетов в основной layout
        self.main_layout.addWidget(self.chats_widget)
        self.main_layout.addWidget(self.chat_widget)
        self.main_layout.addWidget(self.notification_widget)

        # Установка пропорций
        self.main_layout.setStretch(0, 1)  # Чаты
        self.main_layout.setStretch(1, 3)  # Сообщения
        self.main_layout.setStretch(2, 1)  # Уведомления

    def _setup_chats_panel(self):
        """Настройка панели чатов."""
        # Панель иконок
        self._create_icon_panel()

        # Панель заголовка чатов
        self._create_chats_header()

        # Панель фильтров
        self._create_filter_panel()

        # Панель поиска
        self._create_search_panel()

        # Панель сообщений (заглушка)
        self._create_message_panel()

    def _create_icon_panel(self):
        """Создание панели с иконками."""
        icons_widget = QWidget()
        icons_widget.setStyleSheet(Styles['white_widget'])
        icons_layout = QHBoxLayout()
        icons_widget.setLayout(icons_layout)
        self.chats_layout.addWidget(icons_widget)

        # Создание кнопок с иконками
        buttons = [
            ('favourite', ICONS['favourite']),
            ('group', ICONS['group']),
            ('night_theme', ICONS['night_theme']),
            ('customization', ICONS['customization'])
        ]
        for name, icon_path in buttons:
            button = QPushButton()
            button.setFixedSize(50, 50)
            button.setStyleSheet(Styles['icon_button'])
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(32, 32))
            icons_layout.addWidget(button)
            setattr(self, f"{name}_button", button)

        self.chats_layout.setStretch(0, 0)

    def _create_chats_header(self):
        """Создание заголовка панели чатов."""
        header_widget = QWidget()
        header_widget.setStyleSheet(Styles['white_widget'])
        header_layout = QHBoxLayout()
        header_widget.setLayout(header_layout)
        self.chats_layout.addWidget(header_widget)

        # Заголовок "Чаты"
        chats_label = QLabel("Чаты")
        chats_label.setStyleSheet(Styles['chat_label'])
        header_layout.addWidget(chats_label)

        # Кнопка добавления
        add_button = QPushButton()
        add_button.setFixedSize(45, 45)
        add_button.setStyleSheet(Styles['add_button'])
        add_button.setIcon(QIcon(ICONS['add']))
        header_layout.addWidget(add_button)
        self.add_button = add_button

        self.chats_layout.setStretch(1, 0)

    def _create_filter_panel(self):
        """Создание панели фильтров."""
        filter_widget = QWidget()
        filter_widget.setStyleSheet(Styles['white_widget'])
        filter_layout = QHBoxLayout()
        filter_widget.setLayout(filter_layout)
        self.chats_layout.addWidget(filter_widget)

        # Кнопки фильтров
        filter_buttons = [("all", "Все"), ("private", "Приватные"), ("common", "Общие")]
        for name, text in filter_buttons:
            button = QPushButton(text)
            button.setStyleSheet(Styles['filter_button'])
            filter_layout.addWidget(button)
            setattr(self, f"{name}_button", button)

        # Комбобокс "Ещё"
        more_box = QComboBox()
        more_box.addItem("Заявки")
        more_box.addItem("Мои заявки")
        more_box.addItem("Друзья")
        # more_box.model().item(0).setEnabled(False)
        more_box.setFixedHeight(50)
        more_box.setStyleSheet(Styles['combo_box'])
        filter_layout.addWidget(more_box)
        self.more_box = more_box

        self.chats_layout.setStretch(2, 0)

    def _create_search_panel(self):
        """Создание панели поиска."""
        search_widget = QWidget()
        search_widget.setStyleSheet(Styles['white_widget'])
        search_layout = QHBoxLayout()
        search_widget.setLayout(search_layout)
        self.chats_layout.addWidget(search_widget)

        # Поле поиска
        search_input = QLineEdit()
        search_input.setPlaceholderText("Поиск людей и каналов...")
        search_input.setStyleSheet(Styles['search_input'])
        search_action = QAction(QIcon(ICONS['search']), "", search_input)
        search_input.addAction(search_action, QLineEdit.LeadingPosition)
        search_layout.addWidget(search_input)
        self.search_input = search_input

        self.chats_layout.setStretch(3, 0)

    def _create_message_panel(self):
        """Создание панели сообщений (заглушка)."""
        message_widget = QWidget()
        message_widget.setStyleSheet(Styles['white_widget'])
        message_layout = QHBoxLayout()
        message_widget.setLayout(message_layout)
        self.chats_layout.addWidget(message_widget)

        message_label = QLabel()
        message_layout.addWidget(message_label)
        self.message_label = message_label

        self.chats_layout.setStretch(4, 1)

    def _setup_chat_panel(self):
        """Настройка панели чата."""
        # Панель имени контакта
        phone_widget = QWidget()
        phone_widget.setStyleSheet(Styles['white_widget'])
        phone_layout = QHBoxLayout()
        phone_widget.setLayout(phone_layout)
        self.chat_layout.addWidget(phone_widget)

        name_button = QPushButton("Маша Машаева")
        name_button.setStyleSheet(Styles['name_button'])
        phone_layout.addWidget(name_button)
        self.name_button = name_button

        # Панель информации (заглушка)
        info_widget = QWidget()
        info_widget.setStyleSheet(Styles['info_widget'])
        info_layout = QHBoxLayout()
        info_widget.setLayout(info_layout)
        self.chat_layout.addWidget(info_widget)

        self.chat_layout.setStretch(0, 0)

    def _setup_notification_panel(self):
        """Настройка панели уведомлений."""
        notification_label = QLabel("Здесь будут уведомления")
        self.notification_layout.addWidget(notification_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())