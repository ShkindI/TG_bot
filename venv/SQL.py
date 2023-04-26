import sqlite3

con = sqlite3.connect('server.db',check_same_thread=False)

with con:
    con.execute("""CREATE TABLE IF NOT EXISTS Clients(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Adres TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Phone_num BIGINT NOT NULL,
            Sex TEXT NOT NULL,
            Password TEXT NOT NULL,
            Telegram_id BIGINT NOT NULL,
            UNIQUE(Phone_num))""")

    con.execute("""CREATE TABLE IF NOT EXISTS Admins(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Phone_num BIGINT NOT NULL,
                Position INTEGER NOT NULL,
                Telegram_id BIGINT NOT NULL,
                UNIQUE(Phone_num))""")

    con.execute("""CREATE TABLE IF NOT EXISTS Orders(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Client INTEGER NOT NULL,
                Admin INTEGER NOT NULL,
                Date_time TEXT NOT NULL)""")

    con.execute("""CREATE TABLE IF NOT EXISTS Dish(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Price INTEGER NOT NULL,
                Name TEXT NOT NULL, 
                Description TEXT NOT NULL,
                Time_cook INTEGER NOT NULL,
                Admin TEXT NOT NULL,
                Menu_pozition TEXT NOT NULL,
                Stop INTEGER NOT NULL)""")

    con.execute("""CREATE TABLE IF NOT EXISTS Reviews(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Client INTEGER NOT NULL,
                    Grade INTEGER NOT NULL,
                    Review_dish TEXT NOT NULL,
                    Review_servis TEXT NOT NULL,
                    Servis_gradeINTEGER NOT NULL)""")


sql_insert_Clients = "INSERT OR IGNORE INTO Clients (Name, Adres, Age, Phone_num, Sex, Password, Telegram_id) values(?,?,?,?,?,?,?)"
sql_insert_Admins = "INSERT OR IGNORE INTO Admins (Name, Phone_num, Position, Telegram_id) values(?,?,?,?)"
sql_insert_Orders = "INSERT OR IGNORE INTO Orders (Client, Admin, Date_time) values(?,?,CURRENT_TIMESTAMP)"
sql_insert_Dish = "INSERT OR IGNORE INTO Dish (Price, Name, Description, Time_cook, Admin, Menu_pozition, Stop) values(?,?,?,?,?,?,?)"
sql_insert_Reviews = "INSERT OR IGNORE INTO Reviews (Client, Grade, Review_dish, Review_servis, Servis_gradeINTEGER) values(?,?,?,?,?)"


with con:
    con.executemany(sql_insert_Clients,(['Валентина Игоревна','Проспект независимости 123',22,375445678999,'Ж',12345,87654387],
                                        ['Валентина Михайловна','Проспект независимости 120',44,375445674449,'Ж',1234567,67876545],
                                        ['Михаил Андреевич','Проспект независимости 111',32,375448974449,'М',98765,647012861],
                                        ['Иван Андреевич','Проспект независимости 12',28,375448974229,'М',98765,647012866]))

    con.executemany(sql_insert_Admins,(['Синичкина Лера',375333456789,1,647012863],#1 = True Admin
                                       ['Кравченко Татьяна',375333458889,0,76787656],#0 = False Admin
                                       ['Андропова Маша',375443456789,0,67865578]))

    con.executemany(sql_insert_Orders,([2,1],
                                       [1,2]))

    con.executemany(sql_insert_Dish,([23,'Суп том-ям','Суп 1',3,'Шильникова Арина','Суп',0],#1 = Stop
                                     [15,'Ролл Акита','Ролл 1',5,'Кравченко Татьяна','Ролл',0],
                                     [28,'Креветки темпура','Горячее 1',10,'Андропова Маша','Горячее',1],
                                     [10,'Ролл Абури','Ролл 2',6,'Кравченко Татьяна','Ролл',0],
                                     [11,'Ролл Пако','Ролл 3',4,'Кравченко Татьяна','Ролл',1],
                                     [19,'Ролл Мако','Ролл 4',3,'Кравченко Татьяна','Ролл',0],
                                     [13,'Ролл Сосако','Ролл 5',8,'Кравченко Татьяна','Ролл',0],
                                     [12,'Ролл Похуяко','Ролл 6',5,'Кравченко Татьяна','Ролл',1],
                                     [25,'Суп том-кха','Суп 2',5,'Шильникова Арина','Суп',0],
                                     [18,'Суп том-сям','Суп 3',8,'Шильникова Арина','Суп',0],
                                     [22,'Стейк из лосося','Горячее 2',15,'Андропова Маша','Горячее',1],
                                     [35,'Морской гребешок','Горячее 3',15,'Андропова Маша','Горячее',0],
                                     [28,'Стейк','Горячее 4',15,'Андропова Маша','Горячее',0],
                                     [18,'Удон с курицей','Горячее 5',5,'Андропова Маша','Горячее',0]))

    con.executemany(sql_insert_Reviews,([2,5,'Все было очень вкусно, спасибо','Good!',5],
                                        [4,3,'Суп был холодный, долго доставляйте','Bad, very bad!',2]))




