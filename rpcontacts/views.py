# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""
from PyQt5.QtWidgets import (
    QAbstractItemView,          # provide access to to the table view selection behavior policy
    QHBoxLayout,
    QMainWindow,
    QPushButton,                # create the add, delete, and clear all buttons
    QTableView,                 # provide the table-like view that displays the contact list
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget instance
        self.table = QTableView()                                   
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)       
        self.table.resizeColumnsToContents()

        # Create buttons to the GUI
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")

        # create and set a coherent layout for all widgets in the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

