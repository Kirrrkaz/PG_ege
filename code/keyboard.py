from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#button_START = KeyboardButton('Выбрать предметnn')
#START_kb = ReplyKeyboardMarkup(resize_keyboard=True)
#START_kb.add(button_START)

#-----------------------------------------------------------------------------------



START_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_START = KeyboardButton(text='начать', callback_data="button_START")
START_kb.insert(button_START)



mainMenu = InlineKeyboardMarkup(row_width=2)
button_easy = InlineKeyboardButton(text="Лёгкий 🟩🟨", callback_data="button_easy")
button_hard = InlineKeyboardButton(text="Сложный 🟧🟥", callback_data="button_hard")
#button_back_to_main = InlineKeyboardButton(text="назад", callback_data = "button_back_to_main")

mainMenu.insert(button_easy)
mainMenu.insert(button_hard)



ans1 = InlineKeyboardMarkup(row_width=2)
button_a = InlineKeyboardButton(text="а)", callback_data="button_a")
button_b = InlineKeyboardButton(text="б)", callback_data="button_b")
button_v = InlineKeyboardButton(text="в)", callback_data="button_v")
button_g = InlineKeyboardButton(text="г)", callback_data="button_g")

button_back = InlineKeyboardButton(text="Назад", callback_data="button_back")

ans1.insert(button_a)
ans1.insert(button_b)
ans1.insert(button_v)
ans1.insert(button_g)
ans1.insert(button_back)

""" ans2 = InlineKeyboardButton(row_width=2)
button_aa = InlineKeyboardButton(text="а)", callback_data="button_aa")
button_bb = InlineKeyboardButton(text="б)", callback_data="button_bb")
button_vv = InlineKeyboardButton(text="в)", callback_data="button_gg")
button_dd = InlineKeyboardButton(text="г)", callback_data="button_dd")

ans2.insert(button_aa)
ans2.insert(button_bb)
ans2.insert(button_vv)
ans2.insert(button_dd)

ans3 =InlineKeyboardButton(row_width=2)
button_aaa = InlineKeyboardButton(text="а)", callback_data="button_aaa")
button_bbb = InlineKeyboardButton(text="б)", callback_data="button_bbb")
button_vvv = InlineKeyboardButton(text="в)", callback_data="button_ggg")
button_ddd = InlineKeyboardButton(text="г)", callback_data="button_ddd")

ans2.insert(button_aaa)
ans2.insert(button_bbb)
ans2.insert(button_vvv)
ans2.insert(button_ddd)
 """



secondMenu = InlineKeyboardMarkup(row_width=2)



"""
mm = InlineKeyboardMarkup(row_width=2)
button_backk = InlineKeyboardButton(text="назад2", callback_data="button_back2")

mm.insert(button_backk)
"""














#---------------------------------------------------------------------------------------

button_INF = KeyboardButton('Информатика')
INF_kb = ReplyKeyboardMarkup(resize_keyboard=True)
INF_kb.add(button_INF)

button_MATH = KeyboardButton('Математика')
MATH_kb = ReplyKeyboardMarkup(resize_keyboard=True)
MATH_kb.add(button_MATH)

button_RUS = KeyboardButton('Русский язык')
RUS_kb = ReplyKeyboardMarkup(resize_keyboard=True)
RUS_kb.add(button_RUS)

Predmety = ReplyKeyboardMarkup().add(button_INF).add(button_MATH).add(button_RUS)

#------------------------------------------------------------------------------------

button_BACK = KeyboardButton('назад')
BACK_kb = ReplyKeyboardMarkup(resize_keyboard=True)
BACK_kb.add(button_BACK)

button_THEORY = KeyboardButton('теория')
THEORY_kb = ReplyKeyboardMarkup(resize_keyboard=True)
THEORY_kb.add(button_THEORY)


Menushka = ReplyKeyboardMarkup().add(button_BACK).add(button_THEORY)

#------------------------------------------------------------------------------------



#reply_markup=kb.inf_kb, reply_markup=kb.math_kb, reply_markup=kb.rus_kb