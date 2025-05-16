from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from utils.context_util import resource_path
from datetime import datetime


class SearchUserItem(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.init_ui()

    def init_ui(self):
        self.setFixedHeight(60)
        self.setStyleSheet("background-color: white; border-radius: 10px;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        avatar_label = QLabel()
        avatar_label.setFixedSize(40, 40)
        initials = "".join(part[0] for part in self.user.full_name.split()[:2]).upper()
        avatar_label.setText(initials)
        avatar_label.setAlignment(Qt.AlignCenter)
        avatar_label.setStyleSheet("""
            background-color: #706c78;
            border-radius: 20px;
            color: white;
            font-weight: bold;
            font-size: 14px;
        """)
        layout.addWidget(avatar_label)

        text_layout = QVBoxLayout()
        text_layout.setContentsMargins(0, 0, 0, 0)

        name_label = QLabel(self.user.full_name)
        name_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        text_layout.addWidget(name_label)

        try:
            last_seen = datetime.fromisoformat(self.user.last_visit)
            time_str = last_seen.strftime("%H:%M")
        except Exception:
            time_str = "—"

        time_label = QLabel(time_str)
        time_label.setStyleSheet("color: gray; font-size: 12px;")
        text_layout.addWidget(time_label)

        layout.addLayout(text_layout)
        layout.addStretch()