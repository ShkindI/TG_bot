import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputFile

bot = telebot.TeleBot('6247038944:AAG7_JUBj2QxnzadMdffZw4IvkR7SfoE4gc')

dict_titles_for_auth = {}

dict_titles_for_review = {}

orders_dict = {}

stat_dict = {'Roll': [], 'Sup': [], 'Hot': []}

dict_add_new_admin = {'Name': None, 'Phone_num': None, 'Position': None, 'Telegram_id': None}

dict_change_inf_admin = {'Name': None, 'Phone_num': None, 'Position': None}

tg_id_admins_for_change = []

tg_id_admins_for_del = []

cart = []

call_data = []

order = []

timer = []

stop_list = []
not_stop_list = []
