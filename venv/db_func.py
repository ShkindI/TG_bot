import sqlite3
from telegraph import Telegraph
from Storage import dict_titles_for_auth
from Storage import dict_titles_for_review
from Storage import order
from Storage import cart
from Storage import timer
from Storage import orders_dict
from Storage import bot
from Storage import stop_list
from Storage import not_stop_list
from Storage import call_data

con = sqlite3.connect('server.db', check_same_thread=False)
super_admin = 647012863
admin_id = 76787656
client_id = 647012866


def rights_check(id, admin=False, client=False):
    if admin == True:
        try:
            admin = con.execute(f"SELECT Name,Position FROM Admins WHERE Telegram_id = {id}").fetchall()
            return admin[0]
        except:
            return False

    if client == True:
        try:
            client = con.execute(f"SELECT Name FROM Clients WHERE Telegram_id = {id} ").fetchall()
            return client[0]
        except:
            return False


def return_title_for_auth(id):
    with con:
        titles = con.execute("PRAGMA table_info(Clients)")

        for x in titles:
            if x[1] == 'id':
                pass
            elif x[1] == 'Telegram_id':
                dict_titles_for_auth.update({x[1]: id})
            else:
                dict_titles_for_auth.update({x[1]: None})


def return_title_for_review(id):
    with con:
        titles = con.execute('PRAGMA table_info(Reviews)')
        client = con.execute(f"SELECT id FROM Clients WHERE Telegram_id = {id} ").fetchall()
        client_id = 0
        for x in client[0]:
            client_id = x
            break

        for x in titles:
            if x[1] == 'id':
                pass
            elif x[1] == 'Client':
                dict_titles_for_review.update({x[1]: client_id})
            else:
                dict_titles_for_review.update({x[1]: None})
    print(dict_titles_for_review)


def add_new_client(mass):
    sql_insert_Clients = "INSERT OR IGNORE INTO Clients " \
                         "(Name, Adres, Age, Phone_num, Sex, Password, Telegram_id) values(?,?,?,?,?,?,?)"
    with con:
        try:
            con.execute(sql_insert_Clients, (mass))

            return True
        except Exception as e:
            return e


def show_menu(roll=False, sup=False, hot=False):
    data = con.execute("SELECT * FROM Dish")
    if roll == True:
        buffer = []

        for tupl in data.fetchall():
            if tupl[7] == 0:  # Проверяем что блюдо не на стопе!
                for x in tupl:
                    if x == 'Ролл':
                        buffer.append(tupl[2])
        return buffer


    elif sup == True:
        buffer = []

        for tupl in data.fetchall():
            if tupl[7] == 0:  # Проверяем что блюдо не на стопе!
                for x in tupl:
                    if x == 'Суп':
                        buffer.append(tupl[2])
        return buffer
    elif hot == True:
        buffer = []

        for tupl in data.fetchall():
            if tupl[7] == 0:  # Проверяем что блюдо не на стопе!
                for x in tupl:
                    if x == 'Горячее':
                        buffer.append(tupl[2])
        return buffer


def roll(name=None):
    if name == None:
        data = con.execute("SELECT * FROM Dish WHERE Menu_pozition='Ролл'")
        buf = []
        for x in data.fetchall():
            buf.append(x[2])
        return buf
    else:
        data = con.execute(f"SELECT * FROM Dish WHERE Name='{name}'")
        buf = list(data.fetchall()[0])
        res_str = f'Стоимость:  {buf[1]} byn\n' \
                  f'Название:  {buf[2]}\n' \
                  f'Описание блюда:  {buf[3]}\n'
        return res_str


def sup(name=None):
    if name == None:
        data = con.execute("SELECT * FROM Dish WHERE Menu_pozition='Суп'")
        buf = []
        for x in data.fetchall():
            buf.append(x[2])
        return buf
    else:
        data = con.execute(f"SELECT * FROM Dish WHERE Name='{name}'")
        buf = list(data.fetchall()[0])
        res_str = f'Стоимость:  {buf[1]} byn\n' \
                  f'Название:  {buf[2]}\n' \
                  f'Описание блюда:  {buf[3]}\n'
        return res_str


def hot(name=None):
    if name == None:
        data = con.execute("SELECT * FROM Dish WHERE Menu_pozition='Горячее'")
        buf = []
        for x in data.fetchall():
            buf.append(x[2])
        return buf
    else:
        data = con.execute(f"SELECT * FROM Dish WHERE Name='{name}'")
        buf = list(data.fetchall()[0])
        res_str = f'Стоимость:  {buf[1]} byn\n' \
                  f'Название:  {buf[2]}\n' \
                  f'Описание блюда:  {buf[3]}\n'
        return res_str


def admin_contact():
    data = con.execute("SELECT * FROM Admins WHERE Position='1'")

    res_str = ''
    for x in data.fetchall():
        res_str += x[1]
        res_str += '\n'
        res_str += str(x[2])
    return res_str


def check_order(idx, order_list, delivery=False):
    order.append(idx)
    res_str = 'ВНИМАНИЕ, У ВАС НОВЫЙ ЗАКАЗ!\n\n'
    res_str += 'Данные о госте:\n'

    client = con.execute(f"SELECT * FROM Clients WHERE Telegram_id='{idx}'")
    for x in client:
        res_str += f'Имя: {x[1]}\n'
        res_str += f'Адрес: {x[2]}\n'
        res_str += f'Телефон: {x[4]}\n\n'

    res_str += "Позиции меню:\n"
    i = 0
    for x in order_list:
        i += 1
        res_str += f'{i}.{x}\n'
    res_sum = 0
    res_time = 0
    for x in order_list:
        data = con.execute(f"SELECT * FROM Dish WHERE Name='{x}'")
        for i in data:
            res_sum += i[1]
            res_time += i[4]
    if delivery == False:
        res_str += f'Общая стоимость: {res_sum} byn\n'
        res_str += f'Время на приготовление: {res_time} минут\n'
        res_str += f'Тип заказа: Самовывоз\n\n'
        res_str += f'Нажимая кнопку обработан вы, как администратор подтверждайте,' \
                   f'что созвонились с клиентом и сверили правильность всего вышеуказанного!'
        # tik = res_time*60
        tik = 5
        timer.append(tik)
        timer.append(idx)
        cart.clear()
        if idx not in orders_dict.keys():
            orders_dict.update({idx: res_str})
        else:
            orders_dict.pop(idx, None)
            orders_dict.update({idx: res_str})

        return res_str

    else:
        delivery_time = 30
        res_str += f'Общая стоимость: {res_sum} byn\n'
        res_str += f'Время на приготовление: {res_time} минут + {delivery_time} доставка\n'
        res_str += f'Тип заказа: Доставка\n\n'
        res_str += f'Нажимая кнопку обработан вы, как администратор подтверждайте,' \
                   f'что созвонились с клиентом и сверили правильность всего вышеуказанного!'
        # tik = (res_time+delivery_time)*60
        tik = 5
        timer.append(tik)
        timer.append(idx)
        cart.clear()

        if idx not in orders_dict.keys():
            orders_dict.update({idx: res_str})
        else:
            orders_dict.pop(idx, None)
            orders_dict.update({idx: res_str})

        return res_str


def assept_order():
    buf = []

    client = con.execute(f"SELECT id FROM Clients WHERE Telegram_id='{order[0]}'")

    for x in client.fetchall():
        buf.append(x[0])

    admin = con.execute(f"SELECT id FROM Admins WHERE Telegram_id='{order[1]}'")

    for x in admin.fetchall():
        buf.append(x[0])

    sql_insert_Orders = "INSERT OR IGNORE INTO Orders (Client, Admin, Date_time) values(?,?,CURRENT_TIMESTAMP)"
    with con:
        try:
            con.execute(sql_insert_Orders, (buf))
            return True
        except Exception as e:
            return e


def show_card():
    res_str = f'Товаров в корзине: {len(cart)}\n\n'
    for x in cart:
        res_str += f'{x}\n'
    res_str += '\n'
    res_sum = 0
    for x in cart:
        data = con.execute(f"SELECT Price FROM Dish WHERE Name='{x}'")
        for i in data:
            res_sum += i[0]
    res_str += f'Общая сумма к оплате: {res_sum} byn'
    return res_str


def del_from_cart(id=None):
    if id == None:
        for x in cart:
            data = con.execute(f"SELECT id FROM Dish WHERE Name='{x}'")
            for t in data.fetchall():
                t = list(t)
                res_str = ''
                for i in t:
                    i = str(i)
                    res_str += i
                    res_str += 'a'
                call_data.append(res_str)
    else:
        data = con.execute(f"SELECT Name FROM Dish WHERE id='{id}'")
        for t in data.fetchall():
            for i in t:
                return i


# a = del_from_cart()


def add_review():
    buf = []
    sql_insert_Reviews = "INSERT OR IGNORE INTO Reviews " \
                         "(Client, Grade, Review_dish, Review_servis, Servis_gradeINTEGER) values(?,?,?,?,?)"
    for k, v in dict_titles_for_review.items():
        buf.append(v)
    dict_titles_for_review.clear()
    if buf[1] <= 3:
        res_str = "ВНИМАНИЕ\n\n"
        client = con.execute(f"SELECT Name FROM Clients WHERE id='{buf[0]}'")
        for x in client.fetchall():
            res_str += f'Имя: {x[0]}\n'
        res_str += f'Поставил за еду оценку {buf[1]}\n\n Следует обратить на это внимание!'
        bot.send_message("@CrastyCrabsss", res_str)
    if buf[4] <= 3:
        res_str = "ВНИМАНИЕ\n\n"
        client = con.execute(f"SELECT Name FROM Clients WHERE id='{buf[0]}'")
        for x in client.fetchall():
            res_str += f'Имя: {x[0]}\n'
        res_str += f'Поставил за сервис оценку {buf[4]}\n\n Следует обратить на это внимание!'
        bot.send_message("@CrastyCrabsss", res_str)

    with con:
        try:
            con.execute(sql_insert_Reviews, (buf))
            return True
        except Exception as e:
            return e


def add_new_admin(buffer):
    sql_insert_Admins = "INSERT OR IGNORE INTO Admins (Name, Phone_num, Position, Telegram_id) values(?,?,?,?)"

    with con:
        try:
            con.execute(sql_insert_Admins, (buffer))
            return True
        except Exception as e:
            return e


def return_id_name_admin():
    adm_dict = {}
    admins = con.execute("SELECT Telegram_id,Name FROM Admins ")

    for x in admins.fetchall():
        adm_dict.update({x[0]: x[1]})
    return adm_dict


def change_info_adm(tgid, buffer):
    update = f"UPDATE Admins SET name='{buffer[0]}',Phone_num={buffer[1]},Position={buffer[2]} WHERE Telegram_id={tgid}"
    with con:
        try:
            con.execute(update)
            return True
        except Exception as e:
            return e


def del_admin(tgid):
    delete = f"DELETE FROM Admins WHERE Telegram_id = '{tgid}'"
    with con:
        try:
            con.execute(delete)
            return True
        except Exception as e:
            return e


def return_stop_list(stop=None):  # True - возвращает товары на стопе  False - возвращает товары не на стопе!
    res_dict = {}
    if stop == True:
        stop_list.clear()
        data = con.execute("SELECT id,Name FROM Dish WHERE Stop='1'")
        for x in data.fetchall():
            res_dict.update({x[0]: x[1]})
            stop_list.append(str(x[0]))
        return res_dict
    if stop == False:
        not_stop_list.clear()
        data = con.execute("SELECT id,Name FROM Dish WHERE Stop='0'")
        for x in data.fetchall():
            res_dict.update({x[0]: x[1]})
            not_stop_list.append(str(x[0]))
        return res_dict


def Stop_dish(idx, stop=None):  # True - ставим на стоп  False - убираем из стопа!

    if stop == True:
        update = f"UPDATE Dish SET Stop='1' WHERE id={idx}"
        with con:
            try:
                con.execute(update)
                return True
            except Exception as e:
                return e
    if stop == False:
        update = f"UPDATE Dish SET Stop='0' WHERE id={idx}"
        with con:
            try:
                con.execute(update)
                return True
            except Exception as e:
                return e


def return_table_admins_for_qt5():
    with con:
        try:
            data = con.execute("SELECT * FROM Admins")
            titile = con.execute("PRAGMA table_info(Admins)")
            name = []
            for i in titile:
                name.append(i[1])
            return data, name
        except Exception as e:
            return e


def del_admin_id(id):
    delete = f"DELETE FROM Admins WHERE id = '{id}'"
    with con:
        try:
            con.execute(delete)
            return True
        except Exception as e:
            return e


def change_info_admqt5(id, buffer):
    update = f"UPDATE Admins SET name='{buffer[0]}',Phone_num={buffer[1]},Position={buffer[2]},Telegram_id={buffer[3]} WHERE id={id}"
    with con:
        try:
            con.execute(update)
            return True
        except Exception as e:
            return e


def table_dish_for_qt5():  # Глянь тут для ui
    with con:
        try:
            data1 = con.execute("SELECT * FROM Dish")
            titile = con.execute("PRAGMA table_info(Dish)")
            name = []
            for i in titile:
                name.append(i[1])
            return data1, name
        except Exception as e:
            return e


def list_of_admins_for_tg(mess=False, telegraph=False):
    if mess == True:
        buffer = []
        res_str = ""
        data = con.execute("SELECT * FROM Admins")
        for tuplle in data:
            buffer.clear()
            for x in tuplle:
                buffer.append(str(x))
            res_str += f'{buffer[0]}. {buffer[1]}\nТелефонный номер: {buffer[2]}\n'
            if buffer[3] == '1':
                res_str += "Позиция: Старший админ\n"
            else:
                res_str += "Позиция: Младший админ\n"
            res_str += f'Телеграм id: {buffer[4]}\n\n'
        return res_str
    if telegraph == True:
        buffer = []
        res_str = ""
        data = con.execute("SELECT * FROM Admins")
        for tuplle in data:
            buffer.clear()
            for x in tuplle:
                buffer.append(str(x))
            res_str += f'{buffer[0]}. {buffer[1]}\nТелефонный номер: {buffer[2]}\n'
            if buffer[3] == '1':
                res_str += "Позиция: Старший админ\n"
            else:
                res_str += "Позиция: Младший админ\n"
            res_str += f'Телеграм id: {buffer[4]}\n'
        telegraph = Telegraph("913ecf15aa85f04cc93b70e8ec41df5cddc975d322da114685f5ba6c2e7c")
        response = telegraph.create_page(
            'Список админов',
            html_content=f'<p>{res_str}</p>'
        )
        return 'https://telegra.ph/{}'.format(response['path'])
