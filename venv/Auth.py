from Storage import bot
from Storage import InlineKeyboardMarkup
from Storage import InlineKeyboardButton
from Storage import dict_titles_for_auth
from db_func import add_new_client


def auth_new_client_step1(message):
    dict_titles_for_auth['Telegram_id'] = message.chat.id
    dict_titles_for_auth['Name'] = message.text
    msg = bot.send_message(message.chat.id, 'Укажите ваш адрес, что бы мы знали куда привозить вкусняшки:')
    bot.register_next_step_handler(msg, auth_new_client_step2)


def auth_new_client_step2(message):
    dict_titles_for_auth['Adres'] = message.text
    msg = bot.send_message(message.chat.id, 'Укажите ваш полный возраст:')
    bot.register_next_step_handler(msg, auth_new_client_step3)


def auth_new_client_step3(message):
    if message.text.isdigit():
        if int(message.text)<=90:
            dict_titles_for_auth['Age'] = message.text
            msg = bot.send_message(message.chat.id, 'Укажите ваш телефонный номер в формате 375(без знака +):')
            bot.register_next_step_handler(msg, auth_new_client_step4)
        else:
            msg = bot.send_message(message.chat.id, 'Сомневаюсь что вам больше чем 90 лет\n Введите настоящий возраст!')
            bot.register_next_step_handler(msg, auth_new_client_step2)
    else:
        msg = bot.send_message(message.chat.id, 'Только цифры, без букв!')
        bot.register_next_step_handler(msg, auth_new_client_step2)



def auth_new_client_step4(message):
    if message.text.isdigit():
        keyb = InlineKeyboardMarkup()
        keyb.add(InlineKeyboardButton('Я мужчина', callback_data='м'))
        keyb.add(InlineKeyboardButton('Я женщина', callback_data='ж'))
        dict_titles_for_auth['Phone_num'] = message.text
        msg = bot.send_message(message.chat.id, 'Укажите ваш пол:', reply_markup=keyb)
        bot.register_next_step_handler(msg, auth_new_client_step5)

    else:
        msg = bot.send_message(message.chat.id, 'Только числа без + и букв!\n'
                                                'Введите номер телефона: ')
        bot.register_next_step_handler(msg, auth_new_client_step4)


def auth_new_client_step5(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    dict_titles_for_auth['Password'] = message.text
    result_mass = []

    for k, v in dict_titles_for_auth.items():
        if k == 'Age':
            result_mass.append(int(v))
        elif k == 'Phone_num':
            result_mass.append(int(v))
        else:
            result_mass.append(v)

    response = add_new_client(result_mass)

    if response == True:

        bot.send_message(message.chat.id, 'Вы успешно зарегестрированы! Пожалуйста, нажмите кнопку меню'
                                          'и выберите /start что бы начать!')
    else:
        print(response)


