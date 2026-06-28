import sqlite3
import pytest

@pytest.mark.db
def test_sqlite_connection():
    dataTables=sqlite3.connect("D:/Databases/Chinook.db")
    data=dataTables.cursor()
    data.execute('select * from Album where ArtistId = 2')
    results = data.fetchall()
    print(len(results))

