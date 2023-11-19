import sqlite3
from datetime import datetime
import item as itm
import text_templates as tt
from settings import Settings

settings = Settings()

conn = sqlite3.connect("data.db")
c = conn.cursor()


class TN:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"{self.get_tn_id()}"

    def get_tn_id(self):
        return self.id

    def __clist(self):
        c.execute(f"SELECT * FROM tn WHERE tn_id=?", [self.get_tn_id()])
        return list(c)[0]

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
        c.execute(f"UPDATE tn SET item_list=? WHERE tn_id=?",
                  [",".join([str(item.get_id()) for item in item_list + [itm.Item(item_id)]]) if item_list else item_id,
                   self.get_tn_id()])
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
        c.execute(f"UPDATE orders SET item_list=? WHERE tn_id=?",
                  [",".join(item_list) if item_list else "None", self.get_tn_id()])
        conn.commit()

    def get_item_list_amount(self):
        cart = [item.get_id() for item in self.get_item_list()]
        return [[itm.Item(item_id), cart.count(item_id)] for item_id in set(cart)]

    def get_item_list_price(self):
        return sum(
            [item_and_price[0].get_price() * item_and_price[1] for item_and_price in self.get_item_list_amount()]) + (
            float(settings.get_delivery_price()) if self.get_home_adress() != None else 0)

    def set_item_list(self, value):
        c.execute(f"UPDATE orders SET item_list=? WHERE tn_id=?", [value, self.get_tn_id()])
        conn.commit()

    def get_date(self):
        return datetime.strptime(self.__clist()[3], "%Y-%m-%d %H:%M:%S")

    def get_date_string(self):
        return self.__clist()[3]

    def get_manager(self):
        return self.__clist()[1]

    # def set_manager(self, value):
    #     c.execute(f"UPDATE orders SET manager=? WHERE tn_id=?", [value, self.get_tn_id()])
    #     conn.commit()

    # def set_status(self, value):
    #     c.execute(f"UPDATE orders SET status=? WHERE tn_id=?", [value, self.get_tn_id()])
    #     conn.commit()


# def get_status_dict():
#     return {
#         0: tt.processing,
#         1: tt.delivery,
#         2: tt.done,
#         -1: tt.cancelled,
#         -2: tt.cancelled_user,
#     }


def get_tn_list(status=None):
    # if status:
    c.execute(f"SELECT * FROM orders WHERE status=?", [status])
    # else:
    #     c.execute(f"SELECT * FROM orders")
    return list(map(TN, [order[0] for order in list(c)]))


# def get_tn_list_manager(username):
#     # if status:
#     c.execute(f"SELECT * FROM orders WHERE status=? AND manager=?", [2, username])
#     # else:
#     #     c.execute(f"SELECT * FROM orders")
#     return list(map(TN, [order[0] for order in list(c)]))


def does_tn_exist(tn_id):
    c.execute(f"SELECT * FROM tn WHERE tn_id=?", [tn_id])
    return len(list(c)) == 1


def create_tn(manager="None", item_list="None"):
    c.execute(f"INSERT INTO tn(manager, item_list, date) VALUES(?, ?, ?)",
              [manager, item_list, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    conn.commit()


def get_item_list_conf(itm_lst):
    lst = itm_lst.split(",")
    filter_list = []
    for item_list in lst:
        if item_list != "None":
            filter_list.append(str(item_list))
    return list(map(itm.Item, [item_id for item_id in filter_list]))


def remove_from_tn_conf(itm_lst, item_id):
    item_list = [item.get_id() for item in get_item_list_conf(itm_lst)]
    item_list.remove(str(item_id))
    return ",".join(item_list) if item_list else "None"


def get_item_list_amount_conf(itm_lst):
    cart = [item.get_id() for item in get_item_list_conf(itm_lst)]
    return [[itm.Item(item_id), cart.count(item_id)] for item_id in set(cart)]


def get_item_list_price_conf(itm_lst):
    return sum(
        [item_and_price[0].get_price() * item_and_price[1] for item_and_price in itm_lst])
