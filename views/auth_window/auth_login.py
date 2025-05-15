from PyQt5.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QApplication)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_window()

    def _setup_window(self):
        self.setWindowTitle("Аутентификация")
        self.setGeometry(50, 40, 1850, 800)
        self.setStyleSheet()