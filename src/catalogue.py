import sqlite3

from aiogram.types import InputMediaPhoto

import item as itm

conn = sqlite3.connect("data1.db")
c = conn.cursor()

class Catalogue:
    def __init__(self, ctg_id):
        self.id = ctg_id

    def __eq__(self, __o: object) -> bool:
        return self.get_id() == __o.get_id()

    def __repr__(self) -> int:
        return self.get_id()

    def get_id(self):
        return self.id

    def __clist(self):
        c.execute(f"SELECT * FROM catalogue WHERE id=?", [self.get_id()])
        return list(c)[0]

    def get_image_id(self):
        return self.__clist()[1]

    def get_image(self):
        return open("images/" + self.get_image_id(), "rb")

    def set_image_id(self, value):
        c.execute(f"UPDATE catalogue SET image_id=? WHERE id=?", [value, self.get_id()])



def delete(ctg_id):
    c.execute(f"DELETE FROM catalogue WHERE id=?", [ctg_id])
    conn.commit()

def get_ctg_list():
    c.execute(f"SELECT * FROM catalogue")
    return list(map(Catalogue, [cat[0] for cat in list(c)]))

def get_images_list():
    media_group = []
    ctg = get_ctg_list()
    for i in range(len(ctg)):
        url_img = "images/" + ctg.__getitem__(i).get_image_id()
        media_group.append(InputMediaPhoto(open(url_img, "rb"),
                                       caption="" if i == 0 else ''))
    return media_group

def create_ctg(image_id):
    c.execute(f"INSERT INTO catalogue(image_id) VALUES(?)", [image_id])
    conn.commit()


if __name__ == "__main__":
    print(get_ctg_list())