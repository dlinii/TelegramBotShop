import sqlite3
from datetime import datetime
import item as itm
import text_templates as tt
from settings import Settings

settings = Settings()

conn = sqlite3.connect("data.db")
c = conn.cursor()

class Feedback:
    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return f"{self.get_id()}"
    
    def get_id(self):
        return self.id
    
    def __clist(self):
        c.execute(f"SELECT * FROM feedback WHERE id=?", [self.get_id()])
        return list(c)[0]
    
    def get_user_id(self):
        return self.__clist()[1]

    def get_additional_message(self):
        return self.__clist()[2]
    
    def get_date(self):
        return datetime.strptime(self.__clist()[3], "%Y-%m-%d %H:%M:%S")

    def get_date_string(self):
        return self.__clist()[3]

def create_feedback(user_id, additional_message):
    c.execute(f"INSERT INTO feedback(user_id,  additional_message, date) VALUES(?, ?, ?)", [user_id,  additional_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    conn.commit()
    return Feedback(id)