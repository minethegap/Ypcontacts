# -*- coding: utf-8 -*-
# rpcontacts/model.py

"""This module provides a model to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")

        # ensure that the changes on the model get saved into the db 
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    # Inserts a new row at the end of the data model 
    def addContact(self, data):
        """Add a contact to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1 ), field)
        self.model.submitAll()
        self.model.select()

    # Deleting Selected Contacts
    def deleteContact(self, row):
        """Remove a contact from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    # Clearing the Contact Database
    def clearContacts(self):
        """Remove all contacts in the database."""
        # set the data models OnManualSubmit
        # this allows you to cache all the changes until you call submitAll later on
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()

        # reset the model's editStrategy 
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # reloads the data into the model 
        self.model.select()         

