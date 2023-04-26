from Storage import dict_add_new_admin
from Storage import bot
from db_func import add_new_admin

def add_new_admin_step2(message):
    dict_add_new_admin['Name'] = message.text
    msg = bot.send_message(message.chat.id, 'Укажите телефонный номер в формате 375(без знака +):')
    bot.register_next_step_handler(msg, add_new_admin_step3)
def add_new_admin_step3(message):
    if message.text.isdigit():
        dict_add_new_admin['Phone_num'] = int(message.text)
        msg = bot.send_message(message.chat.id, 'Позиция администратора старший или младший?\n\n'
                                                'Введите 1 для старшего\n'
                                                'Введите 0 для младшего')
        bot.register_next_step_handler(msg,add_new_admin_step4)
    else:
        msg = bot.send_message(message.chat.id, 'Только числа без '+' и букв!\n'
                                                'Введите номер телефона: ')
        bot.register_next_step_handler(msg, add_new_admin_step3)
def add_new_admin_step4(message):
    if message.text.isdigit():
        dict_add_new_admin['Position'] = int(message.text)
        msg = bot.send_message(message.chat.id,'Введите телеграм id нового администратора: ')
        bot.register_next_step_handler(msg,add_new_admin_step5)
    else:
        msg = bot.send_message(message.chat.id, 'Только цифры(1 или 0) без букв!')
        bot.register_next_step_handler(msg,add_new_admin_step4)

def add_new_admin_step5(message):
    if message.text.isdigit():
        buffer = []
        dict_add_new_admin['Telegram_id'] = int(message.text)
        print(dict_add_new_admin)
        for k,v in dict_add_new_admin.items():
            buffer.append(v)

        response = add_new_admin(buffer)
        if response == True:
            bot.send_message(message.chat.id,'Добавление прошло успешно!')
        else:
            bot.send_message(message.chat.id,'Произошла техническая ошибка')
            print(response)

    else:
        msg = bot.send_message(message.chat.id, 'Только цифры, без приставки id')
        bot.register_next_step_handler(msg, add_new_admin_step5)


