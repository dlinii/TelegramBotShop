from os import listdir
from aiogram import types
from datetime import datetime

import text_templates as tt
from settings import Settings
import commands
import category
import item
import tn

settings = Settings()

# Back buttons
# Misc
btnBackAdmin = types.InlineKeyboardButton(text=tt.back, callback_data="admin_adminPanel")

# Item management
btnBackItemManagement = types.InlineKeyboardButton(text=tt.back, callback_data="manager_itemManagement")
btnBackEditCatChooseCategory = types.InlineKeyboardButton(text=tt.back, callback_data="manager_editCatChooseCategory")


def btnBackEditCat(cat_id): return types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_editBackCat{cat_id}")


btnBackEditItemChooseCategory = types.InlineKeyboardButton(text=tt.back, callback_data="manager_editItemChooseCategory")


def btnBackEditItemChooseItem(cat_id): return types.InlineKeyboardButton(text=tt.back,
                                                                         callback_data=f"manager_editItemChooseItem{cat_id}")


def btnBackEditItem(item_id): return types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_editItem{item_id}")


# User management
btnBackUserManagement = types.InlineKeyboardButton(text=tt.back, callback_data="admin_userManagement")


def btnBackSeeUserProfile(user_id): return types.InlineKeyboardButton(text=tt.back,
                                                                      callback_data=f"admin_seeUserProfile{user_id}")


def btnBackSeeUserOrders(user_id): return types.InlineKeyboardButton(text=tt.back,
                                                                     callback_data=f"admin_seeUserOrders{user_id}")


# Stats
btnBackShopStats = types.InlineKeyboardButton(text=tt.back, callback_data="admin_shopStats")
btnBackRegistratonStats = types.InlineKeyboardButton(text=tt.back, callback_data="admin_registrationStatsBack")
btnBackOrderStats = types.InlineKeyboardButton(text=tt.back, callback_data="admin_orderStatsBack")

# Settings
btnBackShopSettingsDel = types.InlineKeyboardButton(text=tt.back, callback_data="admin_shopSettingsDel")
btnBackShopSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_shopSettings")
btnBackStatsSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_statsSettings")
btnBackMainSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_mainSettings")
btnBackCheckoutSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_checkoutSettings")
btnBackAdditionalSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_additionalSettings")
btnBackCustomCommands = types.InlineKeyboardButton(text=tt.back, callback_data="admin_customCommands")
btnBackSystemSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_systemSettings")
btnBackItemSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_itemSettings")
btnBackCatalogSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_catalogSettings")
btnBackTypeSettings = types.InlineKeyboardButton(text=tt.back, callback_data="admin_typeSettings")
btnBackBackups = types.InlineKeyboardButton(text=tt.back, callback_data="admin_backups")

# /start menu
btnBackFaq = types.InlineKeyboardButton(text=tt.back, callback_data="faq")
btnBackFaqFeedback = types.InlineKeyboardButton(text=tt.back, callback_data="faq_back")
btnBackFeedback = types.InlineKeyboardButton(text=tt.back, callback_data="feedback_back")
btnBackProfile = types.InlineKeyboardButton(text=tt.back, callback_data="profile")
btnBackProfileState = types.InlineKeyboardButton(text=tt.back, callback_data="profile_back")
btnBackMyOrder = types.InlineKeyboardButton(text=tt.back, callback_data="myOrders")
btnBackCatalogue = types.InlineKeyboardButton(text=tt.back, callback_data="catalogue")


def btnBackViewCat(cat_id): return types.InlineKeyboardButton(text=tt.back, callback_data=f"viewCat{cat_id}")


def btnBackViewItem(item_id): return types.InlineKeyboardButton(text=tt.back, callback_data=f"viewItem{item_id}")
def btnBackViewProfile(user_id): return types.InlineKeyboardButton(text=tt.back, callback_data=f"admin_backViewProfile{user_id}")

btnBackCart = types.InlineKeyboardButton(text=tt.back, callback_data="cart")
btnBackCartDel = types.InlineKeyboardButton(text=tt.back, callback_data="cartDel")
btnBackOrders = types.InlineKeyboardButton(text=tt.back, callback_data="manager_orders")

# Single buttons
btnAdminPanel = types.KeyboardButton(tt.admin_panel)
btnOrders = types.KeyboardButton(tt.orders)
btnManager = types.KeyboardButton(tt.buttonManager)
btnForFooter1 = types.KeyboardButton(tt.profile)
btnForFooter2 = types.KeyboardButton(tt.faq)


def single_button(btn):
    markup = types.InlineKeyboardMarkup()
    markup.add(btn)
    return markup


# Markups
# /start buttons
def get_markup_main():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(tt.catalogue))
    markup.add(types.KeyboardButton(tt.cart))
    # markup.add(types.KeyboardButton(tt.profile), types.KeyboardButton(tt.faq))
    return markup

def get_markup_main_footer():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(tt.profile), types.KeyboardButton(tt.faq))
    return markup

def get_markup_admin():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.item_management, callback_data="manager_itemManagement"))
    markup.add(types.InlineKeyboardButton(text=tt.user_management, callback_data="admin_userManagement"))
    markup.add(types.InlineKeyboardButton(text=tt.shop_stats, callback_data="admin_shopStats"))
    markup.add(types.InlineKeyboardButton(text=tt.bot_settings, callback_data="admin_shopSettings"))
    return markup


def get_markup_faq():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.contacts, callback_data="contacts"))
    markup.add(types.InlineKeyboardButton(text=tt.feedback, callback_data="feedback"))
    # markup.add(types.InlineKeyboardButton(text=tt.refund, callback_data="refund"))
    return markup


def get_markup_comment():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data="cart"))
    markup.add(types.InlineKeyboardButton(text=tt.skip, callback_data="skipComment"))
    return markup


def get_markup_profile(user):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.my_orders, callback_data="myOrders"))
    if user.is_admin() or user.is_manager():
        markup.add(types.InlineKeyboardButton(text=tt.change_price_manager, callback_data="changePriceManager"))
        markup.add(types.InlineKeyboardButton(text=tt.disable_notif if user.notif_on() else tt.enable_notif,
                                              callback_data="changeEnableNotif"))
    return markup


def get_markup_myOrders(order_list):
    markup = types.InlineKeyboardMarkup()
    for order in order_list:
        markup.add(
            types.InlineKeyboardButton(text=order.get_order_id(), callback_data=f"viewMyOrder{order.get_order_id()}"))
    markup.add(btnBackProfile)
    return markup


def get_markup_viewMyOrder(order):
    markup = types.InlineKeyboardMarkup()
    match order.get_status():
        case 0:
            markup.add(types.InlineKeyboardButton(text=tt.cancel_order,
                                                  callback_data=f"cancelUserOrder{order.get_order_id()}"))
        case -2:
            markup.add(
                types.InlineKeyboardButton(text=tt.restore_order, callback_data=f"restoreOrder{order.get_order_id()}"))
    markup.add(btnBackMyOrder)
    return markup


def get_markup_viewNewOrderFromUser(order):
    markup = types.InlineKeyboardMarkup()
    match order.get_status():
        case 0:
            markup.add(types.InlineKeyboardButton(text=tt.cancel_order,
                                                  callback_data=f"cancelUserNewOrder{order.get_order_id()}"))
        case 2:
            markup.add(types.InlineKeyboardButton(text=tt.feedback_for_store, callback_data="feedbackNewOrder"))
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager,
            #                                       callback_data="None"))
            #
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager_img_1, callback_data="None"))
            #
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager_img_2, callback_data="None"))
            #
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager_img_3, callback_data="None"))
            #
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager_img_4, callback_data="None"))
            #
            # markup.add(types.InlineKeyboardButton(text=tt.feedback_for_manager_img_5, callback_data="None"))

        case -1:
            markup.add(types.InlineKeyboardButton(text=tt.feedback_for_store, callback_data="feedbackNewOrder"))
        case -2:
            markup.add(
                types.InlineKeyboardButton(text=tt.restore_order,
                                           callback_data=f"restoreNewOrder{order.get_order_id()}"))
    return markup


def get_markup_cart(user):
    markup = types.InlineKeyboardMarkup()
    # delivery_price = '{:.2f}'.format(float(settings.get_delivery_price()))
    for item_and_amount in user.get_cart_amount():
        cat = category.Category(item_and_amount[0].get_cat_id())
        cat_name = cat.get_name() if len(cat.get_name()) < 15 else (cat.get_name()[:12] + "...")
        item_name = item_and_amount[0].get_name() if len(item_and_amount[0].get_name()) < 24 else (
                item_and_amount[0].get_name()[:21] + "...")
        text = f"{cat_name} - {item_and_amount[0].get_name()} ({item_and_amount[1]}шт.)"
        if len(text) > 47:
            text = f"{cat_name} - {item_name} ({item_and_amount[1]}шт.)"
        markup.add(types.InlineKeyboardButton(
            text=text,
            callback_data=f"viewItem{item_and_amount[0].get_id()}"))

        markup.add(types.InlineKeyboardButton(text=f"{item_and_amount[0].get_price() * item_and_amount[1]}р.",
                                              callback_data="None"), types.InlineKeyboardButton(text=tt.plus,
                                                                                                callback_data=f"addToCartFromCart{item_and_amount[0].get_id()}"),
                   types.InlineKeyboardButton(text=tt.minus,
                                              callback_data=f"removeFromCartFromCart{item_and_amount[0].get_id()}"))
    # if settings.is_delivery_enabled():
    #     markup.add(types.InlineKeyboardButton(text=tt.delivery_on(delivery_price) if user.is_cart_delivery() else tt.delivery_off(delivery_price), callback_data="changeCartDelivery"))
    # else:
    #     markup.add(types.InlineKeyboardButton(text=tt.pickup, callback_data="None"))

    markup.add(types.InlineKeyboardButton(text=tt.clear_cart, callback_data="clearCart"))
    markup.add(
        types.InlineKeyboardButton(text=f"Всего: {'{:.2f}'.format(user.get_cart_price())}р.", callback_data="None"))
    markup.add(types.InlineKeyboardButton(text=tt.cart_checkout, callback_data="checkoutCart"))
    return markup


def get_markup_change_order_item(order):
    markup = types.InlineKeyboardMarkup()
    if order.get_item_list_amount() != "None":
        for item_and_amount in order.get_item_list_amount():
            order_id_and_item_id = f"{order.get_order_id()}_{str(item_and_amount[0].get_id())}"
            cat = category.Category(item_and_amount[0].get_cat_id())
            cat_name = cat.get_name() if len(cat.get_name()) < 15 else (cat.get_name()[:12] + "...")
            item_name = item_and_amount[0].get_name() if len(item_and_amount[0].get_name()) < 24 else (
                    item_and_amount[0].get_name()[:21] + "...")
            text = f"{cat_name} - {item_and_amount[0].get_name()} ({item_and_amount[1]}шт.)"
            if len(text) > 47:
                text = f"{cat_name} - {item_name} ({item_and_amount[1]}шт.)"
            markup.add(types.InlineKeyboardButton(text=text, callback_data=f"viewItem{item_and_amount[0].get_id()}"))
            markup.add(types.InlineKeyboardButton(text=f"{item_and_amount[0].get_price() * item_and_amount[1]}р.",
                                                  callback_data="None"), types.InlineKeyboardButton(text=tt.plus,
                                                                                                    callback_data=f"manager_addToOrderFromOrder{order_id_and_item_id}"),
                       types.InlineKeyboardButton(text=tt.minus,
                                                  callback_data=f"manager_removeFromOrderFromOrder{order_id_and_item_id}"))
    else:
        markup.add(types.InlineKeyboardButton(text=f"Заказ пуст...",
                                              callback_data="None"))

    markup.add(types.InlineKeyboardButton(text=tt.add_item_from_order,
                                          callback_data=f"manager_addItemFromOrder{order.get_order_id()}"))
    if order.get_item_list_amount() != "None":
        markup.add(types.InlineKeyboardButton(text=f"Всего: {'{:.2f}'.format(order.get_item_list_price())}р.",
                                              callback_data="None"))

    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=(
        f"manager_orderChanged{order.get_order_id()}" if order.get_item_list_amount() != "None" else f"manager_changeOrderItem{order.get_order_id()}")))
    return markup


def get_markup_add_tn(item_list):
    markup = types.InlineKeyboardMarkup()
    if item_list != "None":
        for itm in item_list:
            # product = item.Item(itm)
            # order_id_and_item_id = f"{order.get_order_id()}_{str(item_and_amount[0].get_id())}"
            cat = category.Category(itm[0].get_cat_id())
            cat_name = cat.get_name() if len(cat.get_name()) < 15 else (cat.get_name()[:12] + "...")
            item_name = itm[0].get_name() if len(itm[0].get_name()) < 24 else (
                    itm[0].get_name()[:21] + "...")
            text = f"{cat_name} - {itm[0].get_name()} ({itm[1]}шт.)"
            if len(text) > 47:
                text = f"{cat_name} - {item_name} ({itm[1]}шт.)"
            # markup.add(types.InlineKeyboardButton(text=text, callback_data=f"viewItem{itm[0].get_id()}"))
            markup.add(types.InlineKeyboardButton(text=text, callback_data="None"))
            markup.add(types.InlineKeyboardButton(text=f"{itm[0].get_price() * itm[1]}р.",
                                                  callback_data="None"), types.InlineKeyboardButton(text=tt.plus,
                                                                                                    callback_data=f"manager_addCountItemForTN{str(itm[0].get_id())}"),
                       types.InlineKeyboardButton(text=tt.minus,
                                                  callback_data=f"manager_removeCountItemForTN{str(itm[0].get_id())}"))
    else:
        markup.add(types.InlineKeyboardButton(text=f"Товаров нет...",
                                              callback_data="None"))

    markup.add(types.InlineKeyboardButton(text=tt.add_item_from_order,
                                          callback_data=f"manager_addItemFromTN"), types.InlineKeyboardButton(text=tt.add_new_item_from_tn,
                                          callback_data=f"manager_addItem"))
    if item_list != "None":
        markup.add(
            types.InlineKeyboardButton(text=f"Всего: {'{:.2f}'.format(tn.get_item_list_price_conf(item_list))}р.",
                                       callback_data="None"))
        markup.add(types.InlineKeyboardButton(text=tt.create_TN_generate,
                                          callback_data=f"manager_generateTN"))

    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_itemManagement"))
    return markup


def get_markup_addItemToTNChooseCategory(cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"manager_addItemToTNChooseItem{cat.get_id()}"))
    # markup.add(btnBackItemManagement)
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_addTN"))

    return markup

def get_markup_addItemToTNChooseItem(cat):
    markup = types.InlineKeyboardMarkup()
    for product in cat.get_item_list():
        markup.add(types.InlineKeyboardButton(text=f"[{product.get_id()}] {product.get_name()}",
                                              callback_data=f"manager_viewItemFromAddItemToTN{product.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_addItemFromTN"))
    return markup

def get_markup_addItemFromAddItemToTN(item):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.add_to_tn,
                                          callback_data=f"manager_addItemFromAddItemToTN{item.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_addTN"))
    return markup

def get_markup_captcha():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Новая CAPTCHA", callback_data="refreshCaptcha"))
    markup.add(btnBackCartDel)
    return markup


def get_markup_checkoutCartConfirmation():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.confirm, callback_data=f"checkoutCartConfirm"),
               types.InlineKeyboardButton(text=tt.deny, callback_data="cart"))
    return markup


# Catalogue
def get_markup_catalogue(cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        if cat.is_active():
            markup.add(types.InlineKeyboardButton(text=cat.get_name(), callback_data=f"viewCat{cat.get_id()}"))
    # markup.add(types.InlineKeyboardButton(text=tt.search, callback_data="search"))
    return markup


def get_markup_catalogue_img(ctg):
    markup = types.InlineKeyboardMarkup()
    for i in range(len(ctg)):
        markup.add(
            types.InlineKeyboardButton(text=str(i + 1), callback_data=f"deleteImgCtg{ctg.__getitem__(i).get_id()}"))
    return markup


def get_markup_search(query):
    markup = types.InlineKeyboardMarkup()
    for item in query:
        markup.add(types.InlineKeyboardButton(text=item.get_name(), callback_data=f"viewItem{item.get_id()}"))
    markup.add(btnBackCatalogue)
    return markup


def get_markup_viewCat(item_list):
    markup = types.InlineKeyboardMarkup()
    for item in item_list:
        if item.is_active():
            markup.add(types.InlineKeyboardButton(text=f"{item.get_name()} - {item.get_price()} р.",
                                                  callback_data=f"viewItem{item.get_id()}"))
    markup.add(btnBackCatalogue)
    return markup


def get_markup_viewItem(item):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.add_to_cart, callback_data=f"addToCart{item.get_id()}"))
    markup.add(btnBackViewCat(item.get_cat_id()))
    return markup


def get_markup_addItemFromAddItemToOrder(order_id, item):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.add_to_order,
                                          callback_data=f"manager_addItemFromAddItemToOrder{order_id}_{item.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_changeOrderItem{order_id}"))
    return markup


# Admin panel tabs
# Item management
def get_markup_itemManagement():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.add_cat, callback_data="manager_addCat"),
               types.InlineKeyboardButton(text=tt.add_item, callback_data="manager_addItem"))
    markup.add(types.InlineKeyboardButton(text=tt.edit_cat, callback_data="manager_editCatChooseCategory"),
               types.InlineKeyboardButton(text=tt.edit_item, callback_data="manager_editItemChooseCategory"))
    markup.add(types.InlineKeyboardButton(text=tt.add_image_cat, callback_data="manager_addImageCtg"),
               types.InlineKeyboardButton(text=tt.delete_image_cat, callback_data="manager_deleteImageCtg"))
    markup.add(types.InlineKeyboardButton(text=tt.create_TN, callback_data="manager_addTN"),
               types.InlineKeyboardButton(text=tt.generate_text_list_item, callback_data="manager_generateTextListItem"))
    # markup.add(btnBackAdmin)
    return markup


def get_markup_editCatChooseCategory(cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"manager_editCat{cat.get_id()}"))
    markup.add(btnBackItemManagement)
    return markup


def get_markup_editCat(cat_id):
    cat = category.Category(cat_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.change_name, callback_data=f"manager_editCatName{cat_id}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_image, callback_data=f"manager_editCatImage{cat_id}"))
    markup.add(types.InlineKeyboardButton(text=(tt.hide if cat.is_active() else tt.show),
                                          callback_data=f"manager_editHideCat{cat_id}"))
    markup.add(types.InlineKeyboardButton(text=tt.delete, callback_data=f"manager_editCatDelete{cat_id}"))
    markup.add(btnBackEditCatChooseCategory)
    return markup


def get_markup_addItemSetCat(cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"manager_addItemSetCat{cat.get_id()}"))
    markup.add(btnBackItemManagement)
    return markup


btnSkipAddItemSetImage = types.InlineKeyboardButton(text=tt.skip, callback_data="manager_skipSetAddItemSetImage")
btnSkipAddCatSetImage = types.InlineKeyboardButton(text=tt.skip, callback_data="manager_skipSetAddCatSetImage")
def get_markup_userProfileFromBan(user_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.open_profile, callback_data=f"admin_userProfileFromBan{user_id}"))
    return markup

def get_markup_addItemConfirmation():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.confirm, callback_data="manager_addItemConfirm"),
               types.InlineKeyboardButton(text=tt.deny, callback_data="manager_itemManagement"))
    return markup


def get_markup_editItemChooseCategory(cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"manager_editItemChooseItem{cat.get_id()}"))
    markup.add(btnBackItemManagement)
    return markup


def get_markup_addItemToOrderChooseCategory(order_id, cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"manager_addItemToOrderChooseItem{order_id}_{cat.get_id()}"))
    # markup.add(btnBackItemManagement)
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_changeOrderItem{order_id}"))

    return markup


def get_markup_editItemChooseItem(item_list):
    markup = types.InlineKeyboardMarkup()
    for item in item_list:
        markup.add(types.InlineKeyboardButton(text=f"[{item.get_id()}] {item.get_name()}",
                                              callback_data=f"manager_editItem{item.get_id()}"))
    markup.add(btnBackEditItemChooseCategory)
    return markup


def get_markup_addItemToOrderChooseItem(order_id, item_list):
    markup = types.InlineKeyboardMarkup()
    for item in item_list:
        if item.is_active():
            markup.add(types.InlineKeyboardButton(text=f"[{item.get_id()}] {item.get_name()}",
                                                  callback_data=f"manager_viewItemFromAddItemToOrder{order_id}_{item.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_changeOrderItem{order_id}"))
    return markup


async def get_markup_editItem(item):
    itemid = item.get_id()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.change_name, callback_data=f"manager_editItemName{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_image, callback_data=f"manager_editItemImage{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.show_image if await item.is_hide_image() else tt.hide_image,
                                          callback_data=f"manager_editItemHideImage{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_desc, callback_data=f"manager_editItemDesc{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_price, callback_data=f"manager_editItemPrice{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_item_cat, callback_data=f"manager_editItemCat{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_strong, callback_data=f"manager_editItemStrong{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_stock, callback_data=f"manager_editItemStock{itemid}"))
    markup.add(types.InlineKeyboardButton(text=(tt.hide if item.is_active() else tt.show),
                                          callback_data=f"manager_editItemHide{itemid}"))
    markup.add(types.InlineKeyboardButton(text=tt.delete, callback_data=f"manager_editItemDelete{itemid}"))
    markup.add(btnBackEditItemChooseItem(item.get_cat_id()))
    return markup


def get_markup_editItemCat(item_id, cat_list):
    markup = types.InlineKeyboardMarkup()
    for cat in cat_list:
        markup.add(types.InlineKeyboardButton(text=f"[{cat.get_id()}] {cat.get_name()}",
                                              callback_data=f"admin_editItemSetCat{cat.get_id()}"))
    markup.add(btnBackEditItem(item_id))
    return markup


# User management
def get_markup_userManagement():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.user_profile, callback_data="admin_seeUserProfile"))
    markup.add(types.InlineKeyboardButton(text=tt.notify_everyone, callback_data="admin_notifyEveryone"))
    markup.add(types.InlineKeyboardButton(text=tt.refresh_messages, callback_data="admin_refreshMessages"))
    markup.add(btnBackAdmin)
    return markup


def get_markup_notifyEveryoneConfirmation():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.confirm, callback_data="admin_notifyEveryoneConfirm"),
               btnBackUserManagement)
    return markup


def get_markup_seeUserProfile(user):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.orders, callback_data=f"admin_seeUserOrders{user.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.add_black_list if user.is_cart_delivery() else tt.remove_black_list,
                                          callback_data=f"admin_changeIsActiveUser{user.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.remove_manager_role if user.is_manager() else tt.add_manager_role,
                                          callback_data=f"admin_changeUserManager{user.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.remove_admin_role if user.is_admin() else tt.add_admin_role,
                                          callback_data=f"admin_changeUserAdmin{user.get_id()}"))

    markup.add(types.InlineKeyboardButton(text=tt.disable_notif if user.notif_on() else tt.enable_notif,
                                          callback_data=f"admin_changeNotif{user.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_price_manager, callback_data=f"admin_changePriceManager{user.get_id()}"))
    markup.add(btnBackUserManagement)
    return markup


def get_markup_seeUserOrders(user):
    markup = types.InlineKeyboardMarkup()
    for order in user.get_orders():
        markup.add(types.InlineKeyboardButton(text=f"[{order.get_order_id()}]",
                                              callback_data=f"admin_seeUserOrder{order.get_order_id()}"))
    markup.add(btnBackSeeUserProfile(user.get_id()))
    return markup


def get_markup_seeUserOrder(order):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.processing),
                                          callback_data=f"admin_changeOrderStatusProcessing{order.get_order_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.delivery),
                                          callback_data=f"admin_changeOrderStatusDelivery{order.get_order_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.done),
                                          callback_data=f"admin_changeOrderStatusDone{order.get_order_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.cancelled),
                                          callback_data=f"admin_changeOrderStatusCancel{order.get_order_id()}"))

    markup.add(btnBackSeeUserOrders(order.get_user_id()))
    return markup


# Shop stats
def get_markup_shopStats():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.registration_stats, callback_data="admin_registrationStats"))
    markup.add(types.InlineKeyboardButton(text=tt.order_stats, callback_data="admin_orderStats"))
    markup.add(types.InlineKeyboardButton(text=tt.sales_stats, callback_data="admin_salesStats"))
    markup.add(btnBackAdmin)
    return markup


def get_markup_registrationStats():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.all_time, callback_data="admin_registrationStatsAllTime"))
    markup.add(types.InlineKeyboardButton(text=tt.monthly, callback_data="admin_registrationStatsMonthly"))
    markup.add(types.InlineKeyboardButton(text=tt.weekly, callback_data="admin_registrationStatsWeekly"))
    markup.add(types.InlineKeyboardButton(text=tt.daily, callback_data="admin_registrationStatsDaily"))
    markup.add(btnBackShopStats)
    return markup


def get_markup_orderStats():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.all_time, callback_data="admin_orderStatsAllTime"))
    markup.add(types.InlineKeyboardButton(text=tt.monthly, callback_data="admin_orderStatsMonthly"))
    markup.add(types.InlineKeyboardButton(text=tt.weekly, callback_data="admin_orderStatsWeekly"))
    markup.add(types.InlineKeyboardButton(text=tt.daily, callback_data="admin_orderStatsDaily"))
    markup.add(btnBackShopStats)
    return markup


# Shop settings
def get_markup_shopSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.main_settings, callback_data="admin_mainSettings"))
    markup.add(types.InlineKeyboardButton(text=tt.item_settings_catalog, callback_data="admin_catalogSettings"))
    markup.add(types.InlineKeyboardButton(text=tt.item_settings_type, callback_data="admin_typeSettings"))
    markup.add(types.InlineKeyboardButton(text=tt.item_settings, callback_data="admin_itemSettings"))

    markup.add(types.InlineKeyboardButton(text=tt.checkout_settings, callback_data="admin_checkoutSettings"))
    markup.add(types.InlineKeyboardButton(text=tt.stats_settings, callback_data="admin_statsSettings"))
    markup.add(types.InlineKeyboardButton(text=tt.additional_settings, callback_data="admin_additionalSettings"))
    markup.add(btnBackAdmin)
    return markup


def get_markup_mainSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text=f"Название: {settings.get_shop_name()}", callback_data="admin_changeShopName"))
    markup.add(types.InlineKeyboardButton(text=f"Приветствие: {settings.get_shop_greeting()}",
                                          callback_data="admin_changeShopGreeting"))
    # markup.add(types.InlineKeyboardButton(text=f"Политика возврата: {settings.get_refund_policy()}", callback_data="admin_changeShopRefundPolicy"))
    markup.add(types.InlineKeyboardButton(text=f"Контакты: {settings.get_shop_contacts()}",
                                          callback_data="admin_changeShopContacts"))
    markup.add(
        types.InlineKeyboardButton(text=tt.disable_sticker if settings.is_sticker_enabled() else tt.enable_sticker,
                                   callback_data="admin_changeEnableSticker"))
    markup.add(btnBackShopSettings)
    return markup


def get_markup_itemSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        text=tt.disable_item_image if settings.is_item_image_enabled() else tt.enable_item_image,
        callback_data="admin_changeEnableItemImage"))
    markup.add(btnBackShopSettings)
    return markup


def get_markup_catalogSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        text=tt.disable_catalog_image if settings.is_catalog_image_enabled() else tt.enable_catalog_image,
        callback_data="admin_changeEnableCatalogImage"))
    markup.add(btnBackShopSettings)
    return markup


def get_markup_typeSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        text=tt.disable_type_image if settings.is_type_image_enabled() else tt.enable_type_image,
        callback_data="admin_changeEnableTypeImage"))
    markup.add(btnBackShopSettings)
    return markup


def get_markup_checkoutSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.delivery_price('{:.2f}'.format(settings.get_delivery_price())),
                                          callback_data="admin_changeDeliveryPrice"))
    markup.add(
        types.InlineKeyboardButton(text=tt.disable_delivery if settings.is_delivery_enabled() else tt.enable_delivery,
                                   callback_data="admin_changeEnableDelivery"))
    markup.add(types.InlineKeyboardButton(
        text=tt.disable_phone_number if settings.is_phone_number_enabled() else tt.enable_phone_number,
        callback_data="admin_changeEnablePhoneNumber"))
    markup.add(
        types.InlineKeyboardButton(text=tt.disable_captcha if settings.is_captcha_enabled() else tt.enable_captcha,
                                   callback_data="admin_changeEnableCaptcha"))
    markup.add(btnBackShopSettings)
    return markup


def get_markup_statsSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.graph_color, callback_data="admin_statsSettingsColor"))
    markup.add(types.InlineKeyboardButton(text=tt.border_width, callback_data="admin_statsSettingsBorderWidth"))
    markup.add(types.InlineKeyboardButton(text=tt.title_font_size, callback_data="admin_statsSettingsTitleFontSize"))
    markup.add(types.InlineKeyboardButton(text=tt.axis_font_size, callback_data="admin_statsSettingsAxisFontSize"))
    markup.add(types.InlineKeyboardButton(text=tt.tick_font_size, callback_data="admin_statsSettingsTickFontSize"))
    markup.add(btnBackShopSettingsDel)
    return markup


def get_markup_statsSettingsColor():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="⬛️", callback_data="admin_statsSettingsColorBlack"),
               types.InlineKeyboardButton(text="⬜️", callback_data="admin_statsSettingsColorWhite"),
               types.InlineKeyboardButton(text="🟥", callback_data="admin_statsSettingsColorRed"))
    markup.add(types.InlineKeyboardButton(text="🟨", callback_data="admin_statsSettingsColorYellow"),
               types.InlineKeyboardButton(text="🟪", callback_data="admin_statsSettingsColorPurple"),
               types.InlineKeyboardButton(text="🟦", callback_data="admin_statsSettingsColorBlue"))
    markup.add(types.InlineKeyboardButton(text="🟧", callback_data="admin_statsSettingsColorOrange"),
               types.InlineKeyboardButton(text="🟩", callback_data="admin_statsSettingsColorGreen"),
               types.InlineKeyboardButton(text="🟫", callback_data="admin_statsSettingsColorBrown"))
    markup.add(btnBackStatsSettings)
    return markup


def get_markup_statsSettingsBorderWidth():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.unavailable if settings.get_borderwidth() == "0" else tt.minus,
                                          callback_data="None" if settings.get_borderwidth() == "0" else "admin_statsSettingsBorderWidthReduce"),
               types.InlineKeyboardButton(text=settings.get_borderwidth(),
                                          callback_data="admin_statsSettingsBorderWidthDefault"),
               types.InlineKeyboardButton(text=tt.plus, callback_data="admin_statsSettingsBorderWidthAdd"))
    markup.add(btnBackStatsSettings)
    return markup


def get_markup_statsSettingsTitleFontSize():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.unavailable if settings.get_titlefontsize() == "2" else tt.minus,
                                          callback_data="None" if settings.get_titlefontsize() == "2" else "admin_statsSettingsTitleFontSizeReduce"),
               types.InlineKeyboardButton(text=settings.get_titlefontsize(),
                                          callback_data="admin_statsSettingsTitleFontSizeDefault"),
               types.InlineKeyboardButton(text=tt.plus, callback_data="admin_statsSettingsTitleFontSizeAdd"))
    markup.add(btnBackStatsSettings)
    return markup


def get_markup_statsSettingsAxisFontSize():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.unavailable if settings.get_axisfontsize() == "2" else tt.minus,
                                          callback_data="None" if settings.get_axisfontsize() == "2" else "admin_statsSettingsAxisFontSizeReduce"),
               types.InlineKeyboardButton(text=settings.get_axisfontsize(),
                                          callback_data="admin_statsSettingsAxisFontSizeDefault"),
               types.InlineKeyboardButton(text=tt.plus, callback_data="admin_statsSettingsAxisFontSizeAdd"))
    markup.add(btnBackStatsSettings)
    return markup


def get_markup_statsSettingsTickFontSize():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.unavailable if settings.get_tickfontsize() == "2" else tt.minus,
                                          callback_data="None" if settings.get_tickfontsize() == "2" else "admin_statsSettingsTickFontSizeReduce"),
               types.InlineKeyboardButton(text=settings.get_tickfontsize(),
                                          callback_data="admin_statsSettingsTickFontSizeDefault"),
               types.InlineKeyboardButton(text=tt.plus, callback_data="admin_statsSettingsTickFontSizeAdd"))
    markup.add(btnBackStatsSettings)
    return markup


def get_markup_systemSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.clean_images, callback_data="admin_cleanImagesMenu"))
    markup.add(types.InlineKeyboardButton(text=tt.reset_settings, callback_data="admin_resetSettingsMenu"))
    markup.add(types.InlineKeyboardButton(text=tt.clean_database, callback_data="admin_cleanDatabaseMenu"))
    markup.add(types.InlineKeyboardButton(text=tt.clean_logs, callback_data="admin_cleanLogsMenu"))
    markup.add(types.InlineKeyboardButton(text=tt.backups, callback_data="admin_backups"))
    markup.add(types.InlineKeyboardButton(text=tt.disable_debug if settings.is_debug() else tt.enable_debug,
                                          callback_data="admin_changeEnableDebug"))
    markup.add(btnBackAdditionalSettings)
    return markup


def get_markup_backups():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.update_backup, callback_data="admin_updateBackup"))
    markup.add(types.InlineKeyboardButton(text=tt.load_backup, callback_data="admin_loadBackupMenu"))
    markup.add(types.InlineKeyboardButton(text=tt.clean_backups, callback_data="admin_cleanBackupsMenu"))
    markup.add(btnBackSystemSettings)
    return markup


def get_markup_loadBackupMenu():
    markup = types.InlineKeyboardMarkup()
    backups = listdir("backups")
    backups.sort(key=lambda b: datetime.strptime(b, "%d-%m-%Y"))
    for backup in backups[:90]:
        markup.add(types.InlineKeyboardButton(text=backup, callback_data=f"admin_loadBackup{backup}"))
    markup.add(btnBackBackups)
    return markup


def get_markup_cleanBackupsMenu():
    markup = types.InlineKeyboardMarkup()
    for days in ["7", "30", "90"]:
        markup.add(types.InlineKeyboardButton(text=f"{days} дней", callback_data=f"admin_cleanBackups{days}"))
    markup.add(types.InlineKeyboardButton(text="Удалить все резервные копии", callback_data="admin_cleanBackupsAll"))
    markup.add(btnBackBackups)
    return markup


def get_markup_cleanLogsMenu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.delete, callback_data="admin_cleanLogs"))
    markup.add(btnBackSystemSettings)
    return markup


def get_markup_cleanImagesMenu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.delete, callback_data="admin_cleanImages"))
    markup.add(btnBackSystemSettings)
    return markup


def get_markup_resetSettingsMenu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.reset, callback_data="admin_resetSettings"))
    markup.add(btnBackSystemSettings)
    return markup


def get_markup_cleanDatabaseMenu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.delete, callback_data="admin_cleanDatabase"))
    markup.add(btnBackSystemSettings)
    return markup


# Manager tab
def get_markup_seeOrder(order, user_id=None, seeOrder=None):
    markup = types.InlineKeyboardMarkup()
    type_order = "Done"
    if order.get_status() != 0:
        markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.processing),
                                              callback_data=f"manager_changeOrderStatusProcessing{order.get_order_id()}"))
    if order.get_status() != 1:
        markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.delivery),
                                              callback_data=f"manager_changeOrderStatusDelivery{order.get_order_id()}"))
    if order.get_status() != 2:
        markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.done),
                                              callback_data=f"manager_changeOrderStatusDone{order.get_order_id()}"))
    if order.get_status() != -1:
        markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.cancelled),
                                              callback_data=f"manager_changeOrderStatusCancel{order.get_order_id()}"))
    if order.get_status() == 1:
        markup.add(types.InlineKeyboardButton(text=tt.send_msg,
                                              callback_data=f"manager_sendMsgForOrder{order.get_order_id()}"))
        markup.add(types.InlineKeyboardButton(text=tt.change_order_item,
                                              callback_data=f"manager_changeOrderItem{order.get_order_id()}"))
        if order.get_email_adress() is None:
            markup.add(types.InlineKeyboardButton(text=tt.forward_msg,
                                                  callback_data=f"manager_forwardMsgForOrder{order.get_order_id()}"))
    if user_id:
        markup.add(btnBackSeeUserOrders(user_id))
    elif seeOrder != "None":
        match seeOrder:
            case 0:
                type_order = "Processing"
            case 1:
                type_order = "Delivery"
            case 2:
                type_order = "Done"
            case -1:
                type_order = "Cancelled"
            case -2:
                type_order = "CancelledUser"
        markup.add(types.InlineKeyboardButton(text=tt.back, callback_data=f"manager_orders{type_order}"))
    else:
        markup.add(btnBackOrders)

    return markup


def get_markup_seeNewOrder(order, isUnlocked):
    markup = types.InlineKeyboardMarkup()
    if isUnlocked:
        if order.get_status() != 0:
            markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.processing),
                                                  callback_data=f"manager_changeOrderStatusProcessing{order.get_order_id()}"))
        if order.get_status() != 1:
            markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.delivery),
                                                  callback_data=f"manager_changeOrderStatusDelivery{order.get_order_id()}"))
        if order.get_status() != 2:
            markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.done),
                                                  callback_data=f"manager_changeOrderStatusDone{order.get_order_id()}"))
        if order.get_status() != -1:
            markup.add(types.InlineKeyboardButton(text=tt.change_order_status(tt.cancelled),
                                                  callback_data=f"manager_changeOrderStatusCancel{order.get_order_id()}"))
        if order.get_status() == 1:
            markup.add(types.InlineKeyboardButton(text=tt.send_msg,
                                                  callback_data=f"manager_sendMsgForOrder{order.get_order_id()}"))
            markup.add(types.InlineKeyboardButton(text=tt.change_order_item,
                                                  callback_data=f"manager_changeOrderItem{order.get_order_id()}"))
            if order.get_email_adress() is None:
                markup.add(types.InlineKeyboardButton(text=tt.forward_msg,
                                                      callback_data=f"manager_forwardMsgForOrder{order.get_order_id()}"))
    else:
        markup.add(types.InlineKeyboardButton(text=tt.change_order_manager,
                                              callback_data=f"manager_changeOrderOthMng{order.get_order_id()}"))
    return markup


def get_markup_orders():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.processing, callback_data="manager_ordersProcessing"))
    markup.add(types.InlineKeyboardButton(text=tt.delivery, callback_data="manager_ordersDelivery"))
    markup.add(types.InlineKeyboardButton(text=tt.done, callback_data="manager_ordersDone"))
    markup.add(types.InlineKeyboardButton(text=tt.cancelled, callback_data="manager_ordersCancelled"))
    markup.add(types.InlineKeyboardButton(text=tt.cancelled_user, callback_data="manager_ordersCancelledUser"))
    return markup


def get_markup_ordersByOrderList(order_list):
    markup = types.InlineKeyboardMarkup()
    for order in order_list:
        if order.get_manager() == "None" and order.get_additional_message() != "None":
            text = f"№{order.get_order_id()} - {order.get_email_adress()} ({(order.get_additional_message()[:15] + '..') if len(order.get_additional_message()) > 15 else order.get_additional_message()})"
        elif order.get_manager() == "None":
            text = f"№{order.get_order_id()} - {order.get_email_adress()}"
        elif order.get_manager() == order.get_email_adress():
            text = f"№{order.get_order_id()} - {order.get_email_adress()} ({order.get_additional_message()})"
        else:
            text = f"№{order.get_order_id()} - {order.get_email_adress()} ({order.get_manager()})"
        markup.add(types.InlineKeyboardButton(text=text,
                                              callback_data=f"manager_seeOrder{order.get_order_id()}"))
    markup.add(btnBackOrders)
    return markup


def get_markup_additionalSettings():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=tt.custom_commands, callback_data="admin_customCommands"))
    markup.add(types.InlineKeyboardButton(text=tt.system_settings, callback_data="admin_systemSettings"))
    markup.add(btnBackShopSettings)
    return markup


# Custom commands
def get_markup_customCommands():
    markup = types.InlineKeyboardMarkup()
    for command in commands.get_commands():
        markup.add(types.InlineKeyboardButton(text=command.get_command(), callback_data="None"),
                   types.InlineKeyboardButton(text=tt.delete, callback_data=f"admin_deleteCommand{command.get_id()}"))
    markup.add(types.InlineKeyboardButton(text=tt.line_separator, callback_data="None"))
    markup.add(types.InlineKeyboardButton(text=tt.add_command, callback_data="admin_addCommand"))
    markup.add(btnBackAdditionalSettings)
    return markup
