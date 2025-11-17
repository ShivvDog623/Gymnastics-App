import sqlite3
from sqlite3 import Error


class SqliteDBCon:

    def __init__(self):
            self.conn = None
            self.cur = None
            self.setConnection()

    def setConnection(self):
        """
        Establish a database connection to the Sqlite database
        """
        try:
            self.conn = sqlite3.connect('gymnastics_app.db')
            self.cur = self.conn.cursor()
        except Error as e:
            print(e)

    def getConnection(self):
        """
        Get the database connection
        """
        return self.conn
    
    def getCursor(self):
        """
        Get the database cursor
        """
        return self.cur
    
    def closeConnection(self):
        """
        Close the database connection
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed")