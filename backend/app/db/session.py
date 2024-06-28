import sqlite3

def get_db():
    db = sqlite3.connect('simple_erp.db')
    try:
        yield db
    finally:
        db.close()
