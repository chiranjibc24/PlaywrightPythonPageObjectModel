import sqlite3
import pytest

@pytest.mark.db
def test_sqlite_connection():
    dataTables=sqlite3.connect("D:/Databases/Chinook.db")
    