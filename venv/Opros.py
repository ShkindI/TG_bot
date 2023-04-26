from Storage import bot
from Storage import InlineKeyboardMarkup
from Storage import InlineKeyboardButton
from Storage import dict_titles_for_review



def review_step2(message):
    dict_titles_for_review['Review_dish'] = message.text
    msg = bot.send_message(message.chat.id, 'Скажите, вам понравился наш сервис?')
    bot.register_next_step_handler(msg, review_step3)

def review_step3(message):
    dict_titles_for_review['Review_servis'] = message.text
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton('1⭐', callback_data='н'))
    keyb.add(InlineKeyboardButton('2⭐', callback_data='г'))
    keyb.add(InlineKeyboardButton('3⭐', callback_data='ш'))
    keyb.add(InlineKeyboardButton('4⭐', callback_data='щ'))
    keyb.add(InlineKeyboardButton('5⭐', callback_data='з'))
    bot.send_message(message.chat.id, 'Оцените сервис', reply_markup=keyb)




