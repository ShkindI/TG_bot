from Storage import dict_change_inf_admin
from Storage import bot
from db_func import change_info_adm


telgr_id = []




def change_info_admin_step2(message):
    dict_change_inf_admin['Name'] = message.text
    msg = bot.send_message(message.chat.id, 'Укажите телефонный номер в формате 375(без знака +):')
    bot.register_next_step_handler(msg, change_info_admin_step3)

def change_info_admin_step3(message):
    if message.text.isdigit():
        dict_change_inf_admin['Phone_num'] = int(message.text)
        msg = bot.send_message(message.chat.id, 'Позиция администратора старший или младший?\n\n'
                                                'Введите 1 для старшего\n'
                                                'Введите 0 для младшего')
        bot.register_next_step_handler(msg,change_info_admin_step4)
    else:
        msg = bot.send_message(message.chat.id, 'Только числа без '+' и букв!\n'
                                                'Введите номер телефона: ')
        bot.register_next_step_handler(msg, change_info_admin_step3)

def change_info_admin_step4(message):
    if message.text.isdigit():
        buffer = []
        dict_change_inf_admin['Position'] = int(message.text)
        for k,v in dict_change_inf_admin.items():
            buffer.append(v)

        response = change_info_adm(telgr_id[0],buffer)
        if response == True:
            telgr_id.clear()
            bot.send_message(message.chat.id,'Изменения успешно приняты!')

    else:
        msg = bot.send_message(message.chat.id, 'Только цифры(1 или 0) без букв!')
        bot.register_next_step_handler(msg, change_info_admin_step3)
