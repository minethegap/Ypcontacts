# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QtWidget,
}

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        sef.resize(550, 250)
        self.centralWidget = QtWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)


