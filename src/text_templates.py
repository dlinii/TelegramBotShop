from settings import Settings
import category
import order as ordr

settings = Settings()

line_separator = "➖➖➖➖➖"


# Multiple lines
def get_profile_template(user):
    username = f"\n🔖 Никнейм: @{user.get_username()}" if user.get_username() else ""
    price = f"\n💵 Сумма на руках: {0.0 if user.get_price() is None else user.get_price()}р." if (user.is_admin() or user.is_manager()) else ""
    count_sales = f"\n💼 Количество продаж: {len(ordr.get_order_list_manager(user.get_username()))}" if user.is_admin() or user.is_manager() else ""
    return f"{line_separator}\n📝 id: {user.get_id()}\n😄 Имя: {user.get_first()}{username}{price}{count_sales}\n📈 Кол-во заказов: {len(user.get_orders())}\n📅 Дата регистрации: {user.get_register_date_string()}\n{line_separator}"


def get_faq_template(shop_name):
    return f"{line_separator}\n📌 {shop_name}\n📅 EST. Сентябрь 2022г.\n{line_separator}"


def get_categories_template():
    return f"{line_separator}\n🛍️ Категории\n{line_separator}"


def get_category_was_created_successfuly(cat_name):
    return f"Категория {cat_name} была успешно создана."


def get_category_data(cat):
    return f"{line_separator}\nID: {cat.get_id()}\nНазвание: {cat.get_name()}\n{line_separator}"


def get_item_card(item=None, name=None, price=None, desc=None, amount=None, strong=None):
    if item:
        name = item.get_name()
        price = item.get_price()
        desc = item.get_desc()
        amount = item.get_amount()
        strong = item.get_strong()

    return f"{line_separator}\n{name} - {'{:.2f}'.format(price)} р.\nВ наличии: {amount} шт.\n{strong} mg\n{line_separator}\n{desc}"


def get_order_confirmation_template(item_amount_dict, cart_price, additional_message, phone_number=None,
                                    home_adress=None):
    item_amount_dict_formatted = '\n'.join([f'\t· {category.Category(item[0].get_cat_id())} - {item[0].get_name()} {item[0].get_strong} mg ({item[1]} шт.)' for item in item_amount_dict])
    phone_number = f"Номер телефона: {phone_number}\n" if phone_number else ""
    home_adress = f"Адрес доставки: {home_adress}\n" if home_adress else ""
    additional_message = f"Комментарий к заказу: {additional_message}\n" if additional_message else ""
    return f"{line_separator}\nТовары:\n{item_amount_dict_formatted}\nСумма: {cart_price}р.\n{phone_number}{home_adress}{additional_message} \n{line_separator}\nВы уверены, что хотите оформить заказ?"


def get_order_template(order):
    if order.get_item_list_amount() is None:
        item_list_amount_formatted = "-"
    else:
        item_list_amount_formatted = '\n'.join(
            [f'\t· {category.Category(item[0].get_cat_id())} - {item[0].get_name()} {item[0].get_strong} mg ({item[1]} шт.)' for item in order.get_item_list_amount()])
    phone_number = f"Номер телефона: {order.get_phone_number()}\n" if settings.is_phone_number_enabled() else ""
    home_adress = f"Адрес доставки: {order.get_home_adress()}\n" if settings.is_delivery_enabled() else ""
    additional_message = f"Комментарий к заказу: {order.get_additional_message()}\n" if order.get_additional_message() else ""
    status = f"Статус заказа: {order.get_status_string()} - @{order.get_manager()}" if order.get_manager() != "None" else f"Статус заказа: {order.get_status_string()}"
    return f"{line_separator}\nID заказа: {order.get_order_id()}\nID пользователя: {order.get_user_id()}\nТовары:\n{item_list_amount_formatted}\nСумма: {order.get_item_list_price()}р.\nПользователь: @{order.get_email_adress()}\n{phone_number}{home_adress}{additional_message}\n{status}\nДата: {order.get_date_string()}\n{line_separator}"

def get_order_for_user(order):
    if order.get_item_list_amount() is None:
        item_list_amount_formatted = "-"
    else:
        item_list_amount_formatted = '\n'.join(
            [f'\t· {category.Category(item[0].get_cat_id())} - {item[0].get_name()} {item[0].get_strong} mg ({item[1]} шт.)' for item in order.get_item_list_amount()])
    phone_number = f"Номер телефона: {order.get_phone_number()}\n" if settings.is_phone_number_enabled() else ""
    home_adress = f"Адрес доставки: {order.get_home_adress()}\n" if settings.is_delivery_enabled() else ""
    username = f"\nПользователь: @{order.get_email_adress()}" if order.get_email_adress() != "None" else ""
    additional_message = f"Комментарий к заказу: {order.get_additional_message()}\n" if order.get_additional_message() else ""
    status = f"Статус заказа: {order.get_status_string()}. Ваш менеджер: @{order.get_manager()}" if order.get_manager() != "None" else f"Статус заказа: {order.get_status_string()}"

    return f"{line_separator}\nID заказа: {order.get_order_id()}\nТовары:\n{item_list_amount_formatted}\nСумма: {order.get_item_list_price()}р.{username}\n{phone_number}{home_adress}{additional_message}\n{status}\nДата: {order.get_date_string()}\n{line_separator}"


def get_feedback_template(feedback):
    return f"{line_separator}\nID пользователя: {feedback.get_user_id()}\n{feedback.get_additional_message()}\nДата: {feedback.get_date_string()}\n{line_separator}"
def get_order_send_msg(order, username):
    return f"{line_separator}\nПривет, твой заказ №{order.get_order_id()} уже на рассмотрении, но к сожалению у тебя закрытый аккаунт и наш менеджер не может связаться с тобой. Пожалуйста, отпишись менеждеру @{username} для того чтобы договориться о встрече. Спасибо!\n{line_separator}"

def get_sales_stats(users_list):
    all_price = 0.0
    for user in users_list:
        all_price += (0.0 if user.get_price() is None else user.get_price())
    users_and_price = ''.join(
        [f'\t· @{user.get_username()} - {user.get_price()}р.\n' if (0.0 if user.get_price() is None else user.get_price()) > 0.0 else '' for user in
         users_list])
    return f"{line_separator}\nОбщая сумма: {all_price}р.\nСумма у каждого:\n{users_and_price}\n{line_separator}"


# Single phrases
# /start
admin_panel = "🔴 Админ панель"
faq = "ℹ️ FAQ"
profile = "📁 Профиль"
open_profile = "📁 Открыть профиль"
catalogue = "🗄️ Каталог"
cart = "🛒 Корзина"
support_menu = "☎ Меню тех. поддержки"

# Admin panel tabs
item_management = "📦 Управление каталогом"
user_management = "🧍 Управление пользователями"
shop_stats = "📈 Статистика магазина"
bot_settings = "⚙ Настройки бота"

# FAQ
feedback = "💌 Оставить отзыв"
feedback_for_store = "💌 Оставить отзыв магазину"
feedback_for_manager = "Оцените работу менеджера:"
feedback_for_manager_img_1 = "⭐️"
feedback_for_manager_img_2 = "⭐️⭐️"
feedback_for_manager_img_3 = "⭐️⭐️⭐️"
feedback_for_manager_img_4 = "⭐️⭐️⭐️⭐️"
feedback_for_manager_img_5 = "⭐️⭐️⭐️⭐️⭐️"
contacts = "📞 Связаться"
refund = "🎫 Политика возврата"

# Profile
my_orders = "📂 Мои заказы"
cancel_order = "❌ Отменить заказ"
restore_order = "✅ Восстановить заказ"
change_price_manager = "💸 Изменить сумму"
enable_notif = "🔔Включить оповещения о заказах"
disable_notif = "🔕Выключить оповещения о заказах"

# Catalogue / Item / Cart
search = "🔍 Найти"
add_to_cart = "🛒 Добавить в корзину"
add_to_order = "🛒 Добавить в заказ"
cart_is_empty = "Корзина пуста."
pickup = "✅Самовывоз"


def delivery_on(price): return f"✅ Доставка - {price}р."


def delivery_off(price): return f"❌ Доставка - {price}р."


cart_checkout = "Оформить заказ"
change_order_item = "📝 Редактировать заказ"
change_order_manager = "🔐 Изменить статус"
add_item_from_order = "🛒 Добавить товар"
add_new_item_from_tn = "🆕 Новый товар"
clear_cart = "Очистить корзину"
processing = "Обрабатывается"
delivery = "Принят на рассмотрение"
done = "Готов"
cancelled = "Отменён"
cancelled_user = "Отменён пользователем"
send_msg = "Отправить сообщение"
forward_msg = "Переслать сообщения пользователя"

# Item management
add_cat = "🛍️ Добавить категорию"
add_item = "🗃️ Добавить товар"
edit_cat = "✏️ Редактировать категорию"
edit_item = "✏️ Редактировать товар"
add_image_cat = "📁 Добавить фото каталога"
create_TN = "🚛 Товарная накладная"
create_TN_generate = "🚛 Сформировать"
generate_text_list_item = "📊 Наличие товаров"
create_TN_confirm = "Товарная накладная сформирована. Товар добавлен"
add_to_tn = "🛒 Добавить в товарную накладную"
delete_image_cat = "🗑️ Удалить фото каталога"
change_name = "📋 Изменить название"
change_image = "🖼️ Изменить изображение"
hide_image = "🙈 Скрыть изображение"
show_image = "🐵 Показать изображение"
change_desc = "📝 Изменить описание"
change_price = "🏷️ Изменить цену"
change_item_cat = "🛍️ Изменить категорию"
change_stock = "📦 Изменить кол-во"

# User management
user_profile = "📁Профиль пользователя"
notify_everyone = "🔔Оповещение всем пользователям"
refresh_messages = "↩️Переслать сообщения"
orders = "📁 Заказы"
remove_black_list = "👮‍♂️ Убрать из черного списка"
add_black_list = "👮🏿‍♂️ Добавить в черный список"
remove_manager_role = "👨‍💼 Убрать роль менеджера"
add_manager_role = "👨‍💼 Сделать менеджером"
remove_admin_role = "🔴 Убрать роль администратора"
add_admin_role = "🔴 Сделать администратором"


def change_order_status(status): return f"Изменить статус на \"{status}\""


# Shop stats
registration_stats = "👥Статистика регистраций"
order_stats = "📦Статистика заказов"
sales_stats = "🤑Статистика продаж"
all_time = "За всё время"
monthly = "За последние 30 дней"
weekly = "За последние 7 дней"
daily = "За последние 24 часа"

# Shop settings
main_settings = "🛠️ Основные настройки"
item_settings = "🗃️ Настройки товаров"
item_settings_type = "🗃️ Настройки категорий"
item_settings_catalog = "🗃️ Настройки каталога"
additional_settings = "📖 Дополнительные настройки"
custom_commands = "📖 Команды"
add_command = "📝 Добавить команду"
clean_logs = "📖 Очистить логи"
clean_logs_text = "⚠️ Вы уверены, что хотите очистить логи? Они будут удалены без возможности восстановления!\n(Логи за сегодняшний день не будут удалены)"
backups = "💾 Резервное копирование"
update_backup = "🔄 Обновить резервную копию"
load_backup = "💿 Загрузить резервную копию"
clean_backups = "🧹 Очистка резервных копий"
system_settings = "💻 Система"
clean_images = "🗑️ Удалить неиспользуемые изображения"
clean_images_text = "⚠️ Вы уверены, что хотите удалить неспользуемые изображения? Они будут удалены без возможности восстановления!"
clean_database = "📚 Очистить базу данных"
clean_database_text = "⚠️ Вы уверены, что хотите очистить базу данных? Все данные будут удалены без возможности восстановления!"
reset_settings = "⚙️ Сбросить настройки"
resert_settings_text = "⚠️ Вы уверены, что хотите сбросить настройки? Все данные будут удалены без возможности восстановления!"
disable_item_image = "✅ Картинки товаров"
disable_type_image = "✅ Картинки категорий"
disable_catalog_image = "✅ Картинки каталога"
enable_item_image = "❌ Картинки товаров"
enable_type_image = "❌ Картинки категорий"
enable_catalog_image = "❌ Картинки каталога"
checkout_settings = "💳 Настройки оформления заказа"
stats_settings = "📈 Настройки статистики"
graph_color = "🌈 Цвет графика"
border_width = "🔲 Ширина обводки"
title_font_size = "ℹ️ Размер названия графика"
axis_font_size = "↔️Размер текста для осей"
tick_font_size = "🔢Размер текста для делений"
unavailable = "⛔️"
minus = "➖"
plus = "➕"
enable_sticker = "❌ Стикер в приветствии"
disable_sticker = "✅ Стикер в приветствии"
enable_phone_number = "❌ Номер телефона при заказе"
disable_phone_number = "✅ Номер телефона при заказе"
enable_delivery = "❌ Доставка"
disable_delivery = "✅ Доставка"


def delivery_price(price): return f"🚚 Стоимость доставки: {price}р."


enable_captcha = "❌ CAPTCHA при заказе"
disable_captcha = "✅ CAPTCHA при заказе"
enable_debug = "❌ Режим отладки"
disable_debug = "✅ Режим отладки"

# Manager tab
view_order = "📂 Посмотреть заказ"

# Misc buttons
skip = "⏭ Пропустить"
back = "🔙 Назад"
confirm = "✅ Да"
deny = "❌ Нет"
error = "Произошла ошибка!"
or_press_back = "или нажмите на кнопку \"Назад\"."
or_press_cancel = "или нажмите на кнопку \"Отмена\"."
or_press_skip = "или нажмите на кнопку \"Пропустить\"."
hide = "🙈 Скрыть"
show = "🐵 Показать"
delete = "❌ Удалить"
reset = "❌ Сбросить"

if __name__ == "__main__":
    print(delivery_on)
