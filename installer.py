from os import system, name, remove, mkdir, rmdir, listdir
from os.path import exists

import sqlite3


def clearConsole():
    system("cls" if name in ("nt", "dos") else "clear")


def create_config(token, main_admin_id, config_path="config.ini"):
    DEFAULT_CONFIG_TEXT = f"""[main_settings]
token = {token}
mainadminid = {main_admin_id}
debug = 0

[shop_settings]
name = Название магазина
greeting = Добро пожаловать!
refundpolicy = Текст для вкладки "Политика возврата"
contacts = Текст для вкладки "Контакты"
enableimage = 1
enableimagecatalog = 1
enableimagetype = 1
enablesticker = 1
enablephonenumber = 0
enabledelivery = 0
delivery_price = 0.0
enablecaptcha = 0

[stats_settings]
barcolor = 3299ff
borderwidth = 1
titlefontsize = 20
axisfontsize = 12
tickfontsize = 8
"""
    with open(config_path, "w") as config:
        config.write(DEFAULT_CONFIG_TEXT)


CREATE_CATS_TEXT = """
CREATE TABLE "cats" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"image_id"	INTEGER,
	"active"	INTEGER,
	PRIMARY KEY("id")
);
"""
CREATE_ITEMS_TEXT = """
CREATE TABLE "items" (
	"id" INTEGER,
	"name" TEXT NOT NULL,
	"price" FLOAT NOT NULL,
	"cat_id" INTEGER NOT NULL,
	"desc" TEXT,
	"active" INTEGER,
	"amount" INTEGER,
	"image_id" INTEGER,
    "hide_image" INTEGER,
    "strong" INTEGER,
	PRIMARY KEY("id")
)
"""
CREATE_ORDERS_TEXT = """
CREATE TABLE "orders" (
	"order_id" INTEGER,
	"user_id" INTEGER,
	"item_list" TEXT,
	"email_adress" TEXT,
	"phone_number" TEXT,
	"home_adress" TEXT,
	"additional_message" TEXT,
	"date" TEXT,
    "status" INTEGER,
    "manager" INTEGER,
	"notif_adm_msg"	TEXT,
	"id_user_msg" INTEGER
    )
"""
CREATE_USERS_TEXT = """
CREATE TABLE "users" (
	"user_id" INTEGER NOT NULL,
    "username" TEXT, 
	"is_admin" INTEGER,
	"is_manager" INTEGER,
	"notification" INTEGER,
	"date_created" TEXT,
    "cart" TEXT, 
    "cart_delivery" INTEGER,
	"price" FLOAT NOT NULL,
    "first" TEXT
)
"""
CREATE_COMMANDS_TEXT = """
CREATE TABLE "commands" (
    "id" INTEGER NOT NULL,
    "command" TEXT,
    "response" TEXT,
    PRIMARY KEY("id")
)
"""
CREATE_FEEDBACK_TEXT = """
CREATE TABLE "feedback" (
    "id" INTEGER NOT NULL,
    "user_id" INTEGER,
	"additional_message" TEXT,
	"date" TEXT,
    PRIMARY KEY("id")
)
"""
CREATE_CATALOGUE_TEXT = """
CREATE TABLE "catalogue" (
    "id" INTEGER NOT NULL,
    "image_id" TEXT,
    PRIMARY KEY("id")
)
"""
CREATE_TN_TEXT = """
CREATE TABLE "tn" (
	"tn_id" INTEGER NOT NULL,
    "manager" INTEGER,
	"item_list" TEXT,
	"date" TEXT,
    PRIMARY KEY("tn_id")
    )
"""
CREATE_INDEX_FOR_CATALOGUE = """
CREATE INDEX "idx_ctg_img" ON "catalogue" (
	"image_id"	ASC
);
"""
CREATE_INDEX_FOR_CATS = """
CREATE INDEX "idx_cat" ON "cats" (
	"name",
	"image_id"
);
"""


def create_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(CREATE_CATS_TEXT)
    c.execute(CREATE_ITEMS_TEXT)
    c.execute(CREATE_ORDERS_TEXT)
    c.execute(CREATE_USERS_TEXT)
    c.execute(CREATE_COMMANDS_TEXT)
    c.execute(CREATE_FEEDBACK_TEXT)
    c.execute(CREATE_CATALOGUE_TEXT)
    c.execute(CREATE_TN_TEXT)
    c.execute(CREATE_INDEX_FOR_CATALOGUE)
    c.execute(CREATE_INDEX_FOR_CATS)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    clearConsole()
    if any(list(map(exists, ["config.ini", "images", "data.db"]))):
        while True:
            confirmation = input(
                "Вы уверены, что хотите повторно запустить процесс установки? Все данные будут утеряны! (y/N) ")
            if confirmation.lower() in ["y", "yes", "n", "no", ""]:
                break
    else:
        confirmation = "y"

    if confirmation.lower() in ["y", "yes"]:
        print("Вы можете узнать как получить токен бота, перейдя по ссылке: https://youtu.be/fyISLEvzIec")
        token = input("Введите токен бота: ")
        print("Вы можете получить ваш ID, написав \"/start\" боту @userinfobot")
        main_admin_id = input("Введите ID главного администратора: ")
        if main_admin_id.isalnum():
            if exists("data.db"):
                remove("data.db")
                print("База данных была удалена.")
            create_db()
            print("База данных была создана.")
            if exists("config.ini"):
                remove("config.ini")
                print("Файл настроек был удален.")
            create_config(token, main_admin_id)
            print("Файл настроек был создан.")
            if exists("images"):
                for file in listdir("images"):
                    remove("images/" + file)
                rmdir("images")
                print("Папка \"images\" была удалена.")
            mkdir("images")
            print("Папка \"images\" была создана.")
            if exists("backups"):
                for folder in listdir("backups"):
                    for file in listdir("backups/" + folder):
                        remove(f"backups/{folder}/{file}")
                    rmdir(f"backups/{folder}")
                rmdir("backups")
                print("Папка \"backups\" была удалена.")
            mkdir("backups")
            print("Папка \"backups\" была создана.")
            if exists("logs"):
                for file in listdir("logs"):
                    remove("logs/" + file)
                rmdir("logs")
                print("Папка \"logs\" была удалена.")
            mkdir("logs")
            print("Папка \"logs\" была создана.")
        else:
            print("Неверный ID главного администратора.")
    else:
        print("Установка была отменена.")

    input("Нажмите ENTER, чтобы продолжить...")
