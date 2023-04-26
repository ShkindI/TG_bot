import time
import json
from Storage import bot
from Storage import types
from Storage import call_data
from Storage import InlineKeyboardMarkup
from Storage import InlineKeyboardButton
from Storage import dict_titles_for_auth
from Storage import order
from Storage import tg_id_admins_for_change
from Storage import tg_id_admins_for_del
from Storage import stop_list
from Storage import not_stop_list
from Auth import auth_new_client_step1
from Auth import auth_new_client_step5
from db_func import rights_check
from db_func import return_title_for_auth
from db_func import show_menu
from db_func import del_admin
from db_func import roll
from db_func import sup
from db_func import hot
from db_func import del_from_cart
from db_func import return_id_name_admin
from db_func import admin_contact
from db_func import check_order
from db_func import return_stop_list
from db_func import assept_order
from db_func import show_card
from db_func import add_review
from db_func import Stop_dish
from db_func import list_of_admins_for_tg
from Storage import cart
from Storage import timer
from Storage import orders_dict
from Storage import dict_titles_for_review
from db_func import return_title_for_review
from Opros import review_step2
from Statistics import stat
from add_new_admin_tgbot import add_new_admin_step2
from Change_info_admins import telgr_id
from Change_info_admins import change_info_admin_step2
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from threading import Thread


def tg_bot():
    control_panel_admin_true = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add_new_admin = types.KeyboardButton('Добавить нового администратора')
    btn_del_admin = types.KeyboardButton('Удалить администратора')
    btn_change_admin = types.KeyboardButton('Изменить данные о существующем администраторе')
    btn_all_admins = types.KeyboardButton('Хочу увидеть список админов')
    btn_stop_true = types.KeyboardButton('Поставить блюдо на стоп')
    btn_stop_false = types.KeyboardButton('Убрать блюдо из стопа')
    control_panel_admin_true.add(btn_add_new_admin, btn_del_admin, btn_change_admin, btn_all_admins, btn_stop_true,
                                 btn_stop_false)
    control_panel_admin_false = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_stop_true = types.KeyboardButton('Поставить блюдо на стоп')
    btn_stop_false = types.KeyboardButton('Убрать блюдо из стопа')
    control_panel_admin_false.add(btn_stop_true, btn_stop_false)

    @bot.message_handler(content_types=['text'])
    def start(message):
        id = message.from_user.id
        super_admin = 647012863
        admin_id = 76787656
        client_id = 647012866
        if message.text == '/start':

            client = rights_check(id, client=True)

            if client == False:
                keyb = InlineKeyboardMarkup()
                keyb.add(InlineKeyboardButton('Cогласен', callback_data='y'))
                keyb.add(InlineKeyboardButton('Отказываюсь', callback_data='n'))
                bot.send_message(id, "Приветствую, что бы наше общение было приятным и легким,"
                                     "я предлагаю вам зарегестрироваться", reply_markup=keyb)
            else:
                keyb_for_client = InlineKeyboardMarkup()
                keyb_for_client.add(InlineKeyboardButton('Посмотреть меню', callback_data='z'))
                keyb_for_client.add(InlineKeyboardButton('Заказать доставку', callback_data='d'))
                keyb_for_client.add(InlineKeyboardButton('Связаться с администратором', callback_data='c'))

                bot.send_message(id, f'Здравствуйте {client[0]}\n'
                                     f'я вас помню!', reply_markup=keyb_for_client)
        if message.text == '/menu':
            client = rights_check(id, client=True)
            if client == False:
                keyb = InlineKeyboardMarkup()
                keyb.add(InlineKeyboardButton('Cогласен', callback_data='y'))
                keyb.add(InlineKeyboardButton('Отказываюсь', callback_data='n'))
                bot.send_message(id, "Приветствую, что бы наше общение было приятным и легким,"
                                     "я предлагаю вам зарегестрироваться", reply_markup=keyb)
            else:
                menu_keyb = InlineKeyboardMarkup()
                menu_keyb.add(InlineKeyboardButton('Роллы', callback_data='r'))
                menu_keyb.add(InlineKeyboardButton('Супы', callback_data='s'))
                menu_keyb.add(InlineKeyboardButton('Горячие блюда', callback_data='h'))
                bot.send_message(id, 'Выбирай', reply_markup=menu_keyb)
        if message.text == '/admin':
            admin = rights_check(super_admin, admin=True)

            if admin != False and admin[1] == 1:
                # print(f"{admin[0]} You True Admin")
                bot.send_message(id, f'Здравствуйте {admin[0]}', reply_markup=control_panel_admin_true)

            if admin != False and admin[1] == 0:
                # print(f'{admin[0]} You False Admin')
                bot.send_message(id, f'Здравствуйте {admin[0]}', reply_markup=control_panel_admin_false)

        if message.text == 'Добавить нового администратора':
            admin = rights_check(super_admin, admin=True)
            if admin != False and admin[1] == 1:
                msg = bot.send_message(id, 'Введите имя нового администратора: ')
                bot.register_next_step_handler(msg, add_new_admin_step2)
            else:
                # print('У вас недостаточно прав для этого раздела!')
                bot.send_message(id, 'У вас недостаточно прав для этого раздела!')
        # if message.text == '':
        #     pass
        if message.text == 'Изменить данные о существующем администраторе':
            admin = rights_check(super_admin, admin=True)
            if admin != False and admin[1] == 1:
                keyb = InlineKeyboardMarkup()
                d = return_id_name_admin()
                for k, v in d.items():
                    tg_id_admins_for_change.append(str(k))
                    keyb.add(InlineKeyboardButton(v, callback_data=str(k)))
                bot.send_message(id, 'Информацию о каком администраторе вы желайте изменить?', reply_markup=keyb)
            else:
                bot.send_message(id, 'У вас недостаточно прав для этого раздела!')
        if message.text == 'Удалить администратора':
            admin = rights_check(super_admin, admin=True)
            if admin != False and admin[1] == 1:
                keyb = InlineKeyboardMarkup()
                d = return_id_name_admin()
                for k, v in d.items():
                    tg_id_admins_for_del.append(str(k))
                    keyb.add(InlineKeyboardButton(v, callback_data=str(k)))
                bot.send_message(id, 'Какого админа желайте удалить?', reply_markup=keyb)
            else:
                bot.send_message(id, 'У вас недостаточно прав для этого раздела!')
        if message.text == 'Убрать блюдо из стопа':
            admin = rights_check(super_admin, admin=True)

            if admin != False:
                response = return_stop_list(stop=True)
                if response != {}:
                    kb = InlineKeyboardMarkup()
                    for k, v in response.items():
                        kb.add(InlineKeyboardButton(v, callback_data=str(k)))
                    bot.send_message(id, 'список блюд которые на стопе', reply_markup=kb)
                else:
                    bot.send_message(id, 'Таких блюд не оказалось)')

        if message.text == 'Поставить блюдо на стоп':
            admin = rights_check(super_admin, admin=True)

            if admin != False:
                response = return_stop_list(stop=False)
                if response != {}:
                    kb = InlineKeyboardMarkup()
                    for k, v in response.items():
                        kb.add(InlineKeyboardButton(v, callback_data=str(k)))
                    bot.send_message(id, 'список блюд которые не на стопе', reply_markup=kb)
                else:
                    bot.send_message(id, 'Таких блюд не оказалось(')
        if message.text == 'Хочу увидеть список админов':
            admin = rights_check(super_admin, admin=True)
            if admin != False and admin[1] == 1:
                keyb = InlineKeyboardMarkup()
                keyb.add(InlineKeyboardButton('Telegraph', callback_data='т'))
                keyb.add(InlineKeyboardButton('Сообщение', callback_data='ь'))
                bot.send_message(id, 'В каком формате отправить?', reply_markup=keyb)
            else:
                bot.send_message(id, 'У вас недостаточно прав для этого раздела!')

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        bot.answer_callback_query(callback_query_id=call.id, )
        id = call.message.chat.id
        mess_id = call.message.message_id
        flag = call.data[0]
        data = call.data[1:]
        if flag == "y":
            bot.delete_message(chat_id=id, message_id=mess_id)

            return_title_for_auth(id)

            msg = bot.send_message(id, 'Как я могу к вам обращаться?')
            bot.register_next_step_handler(msg, auth_new_client_step1)

        elif flag == 'n':

            bot.send_message(id, 'Хорошо, но если передумайте, используйте команду /start или нажмите Согласен '
                                 'в сообщении выше!\n\n Всего хорошего!')
        elif flag == 'м':#for auth
            dict_titles_for_auth['Sex'] = 'М'
            msg = bot.send_message(id, 'Придумайте пароль для своего профиля:')
            bot.register_next_step_handler(msg, auth_new_client_step5)
        elif flag == 'ж':#for auth
            dict_titles_for_auth['Sex'] = 'Ж'
            msg = bot.send_message(id, 'Придумайте пароль для своего профиля:')
            bot.register_next_step_handler(msg, auth_new_client_step5)
        elif flag == 'z':#default menu
            menu_keyb = InlineKeyboardMarkup()
            menu_keyb.add(InlineKeyboardButton('Роллы', callback_data='r'))
            menu_keyb.add(InlineKeyboardButton('Супы', callback_data='s'))
            menu_keyb.add(InlineKeyboardButton('Горячие блюда', callback_data='h'))
            bot.send_message(id, 'Выбирай', reply_markup=menu_keyb)
        elif flag == 'd':#menu_delivery
            menu_keyb = InlineKeyboardMarkup()
            menu_keyb.add(InlineKeyboardButton('Роллы', callback_data='r'))
            menu_keyb.add(InlineKeyboardButton('Супы', callback_data='s'))
            menu_keyb.add(InlineKeyboardButton('Горячие блюда', callback_data='h'))
            bot.send_message(id, 'Хорошо, что желайте заказать?', reply_markup=menu_keyb)
        elif flag == 'c':#contact with admin
            response = admin_contact()
            bot.send_message(id, f'Вот контакты старшего администратора:\n\n' + response)
        elif flag == 'r':#list_of_rolls
            response = show_menu(roll=True)
            roll_keyb = InlineKeyboardMarkup()
            for x in response:
                roll_keyb.add(InlineKeyboardButton(x, callback_data=str(x)))
            bot.send_message(id, 'Роллы', reply_markup=roll_keyb)
        elif flag == 's':#list_of_sups
            response = show_menu(sup=True)
            sup_keyb = InlineKeyboardMarkup()
            for x in response:
                sup_keyb.add(InlineKeyboardButton(x, callback_data=str(x)))
            bot.send_message(id, 'Супы', reply_markup=sup_keyb)
        if flag == 'h':#list_of_hots
            response = show_menu(hot=True)
            hot_keyb = InlineKeyboardMarkup()
            for x in response:
                hot_keyb.add(InlineKeyboardButton(x, callback_data=str(x)))
            bot.send_message(id, 'Горячие блюда', reply_markup=hot_keyb)
        if call.data in roll():  # Выбор ролла
            stat(id, Roll=True)
            if cart == []:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=roll(name=call.data), reply_markup=add_to_cart_keyb)
            else:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Перейти к оформлению заказа', callback_data='o'))
                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=roll(name=call.data), reply_markup=add_to_cart_keyb)

        elif call.data in sup():  # Выбор супа
            stat(id, Sup=True)
            if cart == []:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=sup(name=call.data), reply_markup=add_to_cart_keyb)
            else:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Перейти к оформлению заказа', callback_data='o'))
                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=sup(name=call.data), reply_markup=add_to_cart_keyb)

        elif call.data in hot():  # Выбор горячего блюда
            stat(id, Hot=True)
            if cart == []:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=hot(name=call.data), reply_markup=add_to_cart_keyb)
            else:
                add_to_cart_keyb = InlineKeyboardMarkup()
                add_to_cart_keyb.add(InlineKeyboardButton('Add to cart', callback_data='k' + call.data))
                add_to_cart_keyb.add(InlineKeyboardButton('Перейти к оформлению заказа', callback_data='o'))

                add_to_cart_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))

                photo = open(f'C:/Users/Shkin/PycharmProjects/TZ01/venv/Фотки для меню/{call.data}.jpg', 'rb')

                bot.send_photo(id, photo=photo, caption=hot(name=call.data), reply_markup=add_to_cart_keyb)
        elif flag == 'k':  # append to cart
            cart.append(data)
            bot.send_message(id, 'Товар успешно добавлен в вашу корзину!')
        elif flag == 'o':  # Доставка или самовывоз
            keyb = InlineKeyboardMarkup()
            keyb.add(InlineKeyboardButton('Доставка', callback_data='l'))
            keyb.add(InlineKeyboardButton('Самовывоз', callback_data='x'))
            bot.send_message(id, 'Желайте доставку или самовывоз?', reply_markup=keyb)
        elif flag == 'u':  # Show the cart
            if cart == []:
                bot.send_message(id, 'Вы туда еще ничего не добавили(')
            else:
                keyb = InlineKeyboardMarkup()
                keyb.add(InlineKeyboardButton('Перейти к оформлению заказа', callback_data='o'))
                keyb.add(InlineKeyboardButton('Удалить блюдо из корзины', callback_data='я'))
                keyb.add(InlineKeyboardButton('Очистить мою корзину', callback_data='ч'))
                response = show_card()
                bot.send_message(id, response, reply_markup=keyb)
        if flag == 'ч':#clean cart
            cart.clear()
            menu_keyb = InlineKeyboardMarkup()
            menu_keyb.add(InlineKeyboardButton('Роллы', callback_data='r'))
            menu_keyb.add(InlineKeyboardButton('Супы', callback_data='s'))
            menu_keyb.add(InlineKeyboardButton('Горячие блюда', callback_data='h'))
            bot.send_message(id, 'Ваша корзину очищена, желайте заказать что-нибудь еще?', reply_markup=menu_keyb)

        if flag == 'я':#del_from_cart(1)
            del_from_cart()
            buf = []
            keyb = InlineKeyboardMarkup()
            print(call_data)
            for x in range(len(cart)):
                keyb.add(InlineKeyboardButton(cart[x], callback_data=call_data[x]))

            bot.send_message(id, 'Какое блюда желайте убрать?', reply_markup=keyb)
        if call.data in call_data: #del_from cart(2)
            name_dish = del_from_cart(id=flag)
            menu_keyb = InlineKeyboardMarkup()
            menu_keyb.add(InlineKeyboardButton('Роллы', callback_data='r'))
            menu_keyb.add(InlineKeyboardButton('Супы', callback_data='s'))
            menu_keyb.add(InlineKeyboardButton('Горячие блюда', callback_data='h'))
            menu_keyb.add(InlineKeyboardButton('Покажи мою корзину', callback_data='u'))
            for x in cart:
                if name_dish == x:
                    cart.remove(x)
            call_data.clear()
            bot.send_message(id, 'Блюдо успешно удалено из корзины!\n\n'
                                 'Желайте заказать что-либо еще?', reply_markup=menu_keyb)

        elif flag == 'l':  # delivery
            bot.delete_message(chat_id=id, message_id=mess_id)
            bot.send_message(id, 'Благодарим вас за заказ\n'
                                 'В ближайшее время с вами свяжется наш администратор для подтверждения заказа\n'
                                 'Желаем вам хорошего дня и приятного аппетита!')
            acept_keyb = InlineKeyboardMarkup()
            acept_keyb.add(InlineKeyboardButton('Обработан', callback_data='a'))
            response = check_order(id, cart, delivery=True)
            bot.send_message("@CrastyCrabsss", response, reply_markup=acept_keyb)


        elif flag == 'x':  # Самовывоз
            bot.delete_message(chat_id=id, message_id=mess_id)
            bot.send_message(id, 'Благодарим вас за заказ\n'
                                 'В ближайшее время с вами свяжется наш администратор для подтверждения заказа\n'
                                 'Желаем вам хорошего дня и приятного аппетита!')
            acept_keyb = InlineKeyboardMarkup()
            acept_keyb.add(InlineKeyboardButton('Обработан', callback_data='a'))
            response = check_order(id, cart, delivery=False)

            bot.send_message("@CrastyCrabsss", response, reply_markup=acept_keyb)
        elif flag == 'a':  # Заказ обработан!
            # order.append(call.from_user.id)
            order.append(647012863)
            response = assept_order()
            if response == True:
                order.clear()
                bot.send_message("@CrastyCrabsss", 'Заказа успешно оформлен!')
                p3.start()
                cart.clear()
            else:
                print(response)
                bot.send_message("@CrastyCrabsss", 'Произошла техническая ошибка\n\n'
                                                   'Вполне вероятно что администратор нажавший "Обработано" не добавлен в базу данных\n\n'
                                                   'Исправьте это и повторите попытку')
        elif flag == 'j':  # Заказа по истечении таймера нет!
            bot.delete_message(chat_id=id, message_id=mess_id)
            for k, v in orders_dict.items():
                if k == id:
                    res_str = 'Заказ опаздывает! Примите меры! Ниже сообщение заказа\n\n\n'
                    res_str += str(v)
                    bot.send_message(id,
                                     'Скоро с вами свяжется наш администрато!\n\nПриносим свои извинения за неудобства!')
                    bot.send_message("@CrastyCrabsss", res_str)
        elif flag == 'v':  # Заказ приехал!
            bot.delete_message(chat_id=id, message_id=mess_id)
            opros = InlineKeyboardMarkup()
            opros.add(InlineKeyboardButton('Согласен, оценю!', callback_data='Y'))
            opros.add(InlineKeyboardButton('Нет, не хочу', callback_data='N'))
            bot.send_message(id, 'Благодарим за то что выбрали наш ресторан!\n\n'
                                 'Уделите нам еще пару минут и оцените наш сервис', reply_markup=opros)
        elif flag == 'N':  # Человек отказался проходить опрос!
            bot.delete_message(chat_id=id, message_id=mess_id)
            bot.send_message(id, 'Спасибо, приятного аппетита и спасибо что заказали именно у нас!')
        elif flag == 'Y':  # Опрос начинается!
            bot.delete_message(chat_id=id, message_id=mess_id)
            return_title_for_review(id)
            keyb = InlineKeyboardMarkup()
            keyb.add(InlineKeyboardButton('1⭐', callback_data='й'))
            keyb.add(InlineKeyboardButton('2⭐', callback_data='ц'))
            keyb.add(InlineKeyboardButton('3⭐', callback_data='у'))
            keyb.add(InlineKeyboardButton('4⭐', callback_data='к'))
            keyb.add(InlineKeyboardButton('5⭐', callback_data='е'))
            bot.send_message(id, 'Пожалуйста, оцените наши блюда', reply_markup=keyb)

        if flag == 'й':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Grade'] = 1
            msg = bot.send_message(id, 'Напишите краткий отзыв о еде,почему именно такую оценку вы указали:')

            bot.register_next_step_handler(msg, review_step2)
        if flag == 'ц':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Grade'] = 2
            msg = bot.send_message(id, 'Напишите краткий отзыв о еде,почему именно такую оценку вы указали:')
            bot.register_next_step_handler(msg, review_step2)
        if flag == 'у':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Grade'] = 3
            msg = bot.send_message(id, 'Напишите краткий отзыв о еде,почему именно такую оценку вы указали:')
            bot.register_next_step_handler(msg, review_step2)
        if flag == 'к':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Grade'] = 4
            msg = bot.send_message(id, 'Напишите краткий отзыв о еде,почему именно такую оценку вы указали:')
            bot.register_next_step_handler(msg, review_step2)
        if flag == 'е':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Grade'] = 5
            msg = bot.send_message(id, 'Напишите краткий отзыв о еде, почему именно такую оценку вы указали:')
            bot.register_next_step_handler(msg, review_step2)
        if flag == 'н':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Servis_gradeINTEGER'] = 1
            response = add_review()
            bot.send_message(id,
                             'Благодарим за внимание\n\n Ждем вас снова в крастикрабс\n\n И помните, нам важны не вы, а ваши деньги:)')
        if flag == 'г':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Servis_gradeINTEGER'] = 2
            response = add_review()
            bot.send_message(id,
                             'Благодарим за внимание\n\n Ждем вас снова в крастикрабс\n\n И помните, нам важны не вы, а ваши деньги:)')
        if flag == 'ш':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Servis_gradeINTEGER'] = 3
            response = add_review()
            bot.send_message(id,
                             'Благодарим за внимание\n\n Ждем вас снова в крастикрабс\n\n И помните, нам важны не вы, а ваши деньги:)')

        if flag == 'щ':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Servis_gradeINTEGER'] = 4
            response = add_review()
            bot.send_message(id,
                             'Благодарим за внимание\n\n Ждем вас снова в крастикрабс\n\n И помните, нам важны не вы, а ваши деньги:)')

        if flag == 'з':
            bot.delete_message(chat_id=id, message_id=mess_id)
            dict_titles_for_review['Servis_gradeINTEGER'] = 5
            response = add_review()
            bot.send_message(id,
                             'Благодарим за внимание\n\n Ждем вас снова в крастикрабс\n\n И помните, нам важны не вы, а ваши деньги:)')

        if call.data in tg_id_admins_for_change:
            telgr_id.append(call.data)
            msg = bot.send_message(id, 'Введите имя администратора: ')
            bot.register_next_step_handler(msg, change_info_admin_step2)
        if call.data in tg_id_admins_for_del:
            response = del_admin(call.data)
            if response == True:
                bot.send_message(id, 'Удаление прошло успешно!')
            else:
                bot.send_message(id, 'error')
                print(response)

        if call.data in stop_list:
            response = Stop_dish(call.data, stop=False)
            if response == True:
                bot.send_message(id, 'Блюдо успешно вычеркнуто из стопа, оно отобразится в меню!')
            else:
                bot.send_message(id, 'error')
        if call.data in not_stop_list:
            response = Stop_dish(call.data, stop=True)
            if response == True:
                bot.send_message(id, 'Блюдо успешно добавлено в стоп лист!')
            else:
                bot.send_message(id, 'error')
                print(response)
        if flag == 'т':
            response = list_of_admins_for_tg(telegraph=True)
            bot.send_message(id, response)
        if flag == 'ь':
            response = list_of_admins_for_tg(mess=True)
            bot.send_message(id, response)

    print("Ready")
    bot.infinity_polling()


def vk_bot():  # Всратое нежизнеспособное говнище...
    GROUP_ID = '218746134'
    GROUP_TOKEN = 'vk1.a.Q59deh2Wus-arbiLhiQHmGyzKS43tS_OldxejCmj0pVhJd7RzCHRTq53w8jShJh8RJTtexg1J91DupxHQfCG_l1zWXZ-Mj0OWXgJ_sybz66LI0bHz2mj6QfFBtia020jVxwvZIIxKrkxaHKSPJACDT2530qy107t8J5c2C6OQ9fs3GwHu-XSLHAd83_Ik46i1mEIUlEwXzVSjTa3LMUBJQ'
    API_VERSION = '5.120'

    settings = dict(one_time=False, inline=False)
    settings2 = dict(one_time=False, inline=True)

    start_keyb = VkKeyboard(**settings)
    start_keyb.add_button(label='Запустить бота!', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
    start_keyb.add_line()
    start_keyb.add_callback_button(label='Мы в Телеграме!', color=VkKeyboardColor.PRIMARY,
                                   payload={"type": "open_link", "link": "https://t.me/Mishlen_restoran_Bot"})

    vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

    CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app', 'text')

    HI = []
    HI.append("start")
    HI.append("Start")
    HI.append("начать")
    HI.append("Начало")
    HI.append("Начать")
    HI.append("начало")
    HI.append("Бот")
    HI.append("бот")
    HI.append("Старт")
    HI.append("старт")
    HI.append("скидки")
    HI.append("Скидки")

    START_TXT = '1. Для начала работы нажмите : "Запустить бота!😉'

    print("Ready!")

    Category_menu = ['Roll', 'Sup', 'Hot']
    Roll_list = []
    Sup_list = []
    Hot_list = []

    def gen_keyb(list, type, fix_poz=5, num=0):
        keyb = VkKeyboard(**settings2)
        if ((num + 1) * fix_poz) < len(list):
            end_ = ((num + 1) * fix_poz)
        else:
            end_ = len(list)
        for x in range(num * fix_poz, end_):
            keyb.add_button(label=list[x], color=VkKeyboardColor.SECONDARY, payload={"type": list[x]})
            keyb.add_line()
        if num == 0:
            num += 1
            keyb.add_callback_button(label='Далее', color=VkKeyboardColor.PRIMARY,
                                     payload={"type": type, "num": num})
        elif num != 0 and end_ == len(list):
            num -= 1
            keyb.add_callback_button(label='Назад', color=VkKeyboardColor.PRIMARY,
                                     payload={"type": type, "num": num})
        else:
            var1 = num + 1
            var2 = num - 1
            keyb.add_callback_button(label='Далее', color=VkKeyboardColor.PRIMARY,
                                     payload={"type": type, "num": var1})
            keyb.add_callback_button(label='Назад', color=VkKeyboardColor.PRIMARY,
                                     payload={"type": type, "num": var2})
        return keyb

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                if event.obj.message['text'] in HI:
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=start_keyb.get_keyboard(),
                        message=START_TXT)
                if event.obj.message['text'] == 'Запустить бота!':
                    K = gen_keyb(Category_menu, 'Category')
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=K.get_keyboard(),
                        message='Вот категории нашего меню!')
                elif event.obj.message['text'] in Category_menu:

                    if event.obj.message['text'] == 'Roll':
                        response = show_menu(roll=True)
                        for x in response:
                            Roll_list.append(x)
                        K = gen_keyb(response, 'Roll')
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            keyboard=K.get_keyboard(),
                            message='Rolls')

                    if event.obj.message['text'] == 'Sup':
                        response = show_menu(sup=True)
                        for x in response:
                            Sup_list.append(x)
                        K = gen_keyb(response, 'Sup')
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            keyboard=K.get_keyboard(),
                            message='Sups')

                    if event.obj.message['text'] == 'Hot':
                        response = show_menu(hot=True)
                        for x in response:
                            Hot_list.append(x)
                        K = gen_keyb(response, 'Hots')
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            keyboard=K.get_keyboard(),
                            message='Hots')







        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == "Roll":
                K = gen_keyb(Category_menu, "Roll", num=event.object.payload.get('num'))
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message='Rolls',
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=K.get_keyboard())
            elif event.object.payload.get('type') == "Sup":
                K = gen_keyb(Category_menu, "Sup", num=event.object.payload.get('num'))
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message='Sups',
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=K.get_keyboard())
            elif event.object.payload.get('type') == "Hot":
                K = gen_keyb(Category_menu, "Hot", num=event.object.payload.get('num'))
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message='Hots',
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=K.get_keyboard())
            elif event.object.payload.get('type') in CALLBACK_TYPES:
                vk.messages.sendMessageEventAnswer(
                    event_id=event.object.event_id,
                    user_id=event.object.user_id,
                    peer_id=event.object.peer_id,
                    event_data=json.dumps(event.object.payload))


def Timer():
    idx = timer[1]
    time.sleep(timer[0])
    zakaz = InlineKeyboardMarkup()
    zakaz.add(InlineKeyboardButton('Заказ приехал!', callback_data='v'))
    zakaz.add(InlineKeyboardButton('Заказа до сих пор нет!', callback_data='j'))
    bot.send_message(idx, 'Время ожидания вашего заказа истекло\n\n Пожалуйста выберите один из вариантов ниже',
                     reply_markup=zakaz)


p1 = Thread(target=tg_bot)

p2 = Thread(target=vk_bot)

p3 = Thread(target=Timer)  # На второй заказ не открывается если не завершать поток!


