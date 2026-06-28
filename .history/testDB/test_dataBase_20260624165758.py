import sqlite3
import pytest

@pytest.mark.db
def test_sqlite_connection():
    dataTables=sqlite3.connect("D:/Databases/Chinook.db")
    data=dataTables.cusror()
    data.execute("select * from Album")
    results=data.fe