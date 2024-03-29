import sqlite3
from datetime import datetime
import item as itm
import text_templates as tt
from settings import Settings

settings = Settings()

conn = sqlite3.connect("data.db")
c = conn.cursor()

class Order:
    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return f"{self.get_order_id()}"
    
    def get_order_id(self):
        return self.id
    
    def __clist(self):
        c.execute(f"SELECT * FROM orders WHERE order_id=?", [self.get_order_id()])
        return list(c)[0]
    
    def get_user_id(self):
        return self.__clist()[1]
    
    def get_item_list_raw(self):
        return self.__clist()[2]
    
    def get_item_list(self):
        lst = self.get_item_list_raw().split(",")
        filter_list = []
        for item_list in lst:
            if item_list != "None":
                filter_list.append(str(item_list))
        return list(map(itm.Item, [item_id for item_id in filter_list]))

    def get_count_item_list(self, item_id):
        items = self.get_item_list()
        count = 0
        for itm_cart in items:
            if str(itm_cart.get_id()) == str(item_id):
                count += 1
        return count

    def get_item_id_list(self):
        cart = [item.get_id() for item in self.get_item_list()]
        return cart
    def add_to_order(self, item_id):
        item_list = self.get_item_list()
        c.execute(f"UPDATE orders SET item_list=? WHERE order_id=?",
                  [",".join([str(item.get_id()) for item in item_list + [itm.Item(item_id)]]) if item_list else item_id,
                   self.get_order_id()])
        conn.commit()

    def get_count_item_order_for_id(self, item_id):
        cart = self.get_item_id_list()
        count = 0
        for itm_cart in cart:
            if itm_cart == item_id:
                count += 1
        return count

    def remove_from_order(self, item_id):
        item_list = [item.get_id() for item in self.get_item_list()]
        item_list.remove(str(item_id))
        c.execute(f"UPDATE orders SET item_list=? WHERE order_id=?", [",".join(item_list) if item_list else "None", self.get_order_id()])
        conn.commit()

    def get_item_list_amount(self):
        cart = [item.get_id() for item in self.get_item_list()]
        return [[itm.Item(item_id), cart.count(item_id)] for item_id in set(cart)]
    
    def get_item_list_price(self):
        return sum([item_and_price[0].get_price() * item_and_price[1] for item_and_price in self.get_item_list_amount()]) + (float(settings.get_delivery_price()) if self.get_home_adress() != None else 0)
    
    def set_item_list(self, value):
        c.execute(f"UPDATE orders SET item_list=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
    def get_email_adress(self):
        return self.__clist()[3]
    
    def set_email_adress(self, value):
        c.execute(f"UPDATE orders SET email_adress=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
    def get_phone_number(self):
        return self.__clist()[4]
    
    def set_phone_number(self, value):
        c.execute(f"UPDATE orders SET phone_number=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
    def get_home_adress(self):
        return self.__clist()[5]
    
    def set_home_adress(self, value):
        c.execute(f"UPDATE orders SET home_adress=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
    def get_additional_message(self):
        return self.__clist()[6]
    
    def get_date(self):
        return datetime.strptime(self.__clist()[7], "%Y-%m-%d %H:%M:%S")

    def get_date_string(self):
        return self.__clist()[7]
    
    def get_status(self):
        return self.__clist()[8]
    
    def get_status_string(self):
        return get_status_dict()[self.__clist()[8]]

    def get_notif_adm_msg_string(self):
        return self.__clist()[10]

    def get_id_user_msg(self):
        return self.__clist()[11]

    def get_notif_adm_msg_list(self):
        _str = self.get_notif_adm_msg_string()
        _list = _str.split(",")
        return _list

    def set_notif_adm_msg_str(self, value):
        c.execute(f"UPDATE orders SET notif_adm_msg=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()

    def set_id_user_msg(self, value):
        c.execute(f"UPDATE orders SET id_user_msg=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()

    def get_manager(self):
        return self.__clist()[9]
    def set_manager(self, value):
        c.execute(f"UPDATE orders SET manager=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
    def set_status(self, value):
        c.execute(f"UPDATE orders SET status=? WHERE order_id=?", [value, self.get_order_id()])
        conn.commit()
    
def get_status_dict():
    return {
            0: tt.processing,
            1: tt.delivery,
            2: tt.done,
            -1: tt.cancelled,
            -2: tt.cancelled_user,
        }

def get_order_list(status=None):
    if status == 2:
        c.execute(f"SELECT * FROM orders WHERE status=? limit 50", [status])
    else:
        c.execute(f"SELECT * FROM orders WHERE status=?", [status])
    return list(map(Order, [order[0] for order in list(c)]))

def get_order_list_manager(username):
    # if status:
    c.execute(f"SELECT * FROM orders WHERE status=? AND manager=?", [2, username])
    # else:
    #     c.execute(f"SELECT * FROM orders")
    return list(map(Order, [order[0] for order in list(c)]))

def does_order_exist(order_id):
    c.execute(f"SELECT * FROM orders WHERE order_id=?", [order_id])
    return len(list(c)) == 1
    
def create_order(order_id, user_id, item_list, email_adress, additional_message, phone_number="None", home_adress="None", manager="None", notif_adm_msg="None", id_user_msg="None"):
    c.execute(f"INSERT INTO orders VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [order_id, user_id, item_list, email_adress, phone_number, home_adress, additional_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, manager, notif_adm_msg, id_user_msg])
    conn.commit()
    return Order(order_id)