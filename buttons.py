from telebot import types


# Кнопка для отправки номера
def num_button():
    # Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки
    but1 = types.KeyboardButton('Отправить номер📞',
                                request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(but1)
    return kb
# кнопки для
def language_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Russian_language = types.KeyboardButton('Русский язык')
    English_language = types.KeyboardButton('Английский язык')
    Uzbek_language = types.KeyboardButton('узбекский язык')


    # Добавляем кнопки в пространство
    kb.add()

# Кнопка для отправки локации
def loc_button():
    # Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки
    but1 = types.KeyboardButton('Отправить геопозоцию📌',
                                request_location=True)
    # Добавляем кнопки в пространство
    kb.add(but1)
    return kb


# Кнопки админ-меню
def admin_menu():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    add = types.KeyboardButton('Добавить продукт')
    delete = types.KeyboardButton('Удалить продукт')
    change = types.KeyboardButton('Изменить количество')
    back = types.KeyboardButton('Обратно в меню')
    # Добавляем кнопки в пространство
    kb.add(add, delete, change)
    kb.row(back)
    return kb


# Кнопки для подтверждения
def confirm_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    # Добавляем кнопки в пространство
    kb.add(yes, no)

# кнопки вывода товаров

def pr_buttons(products):
    # создаем пронстранство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем кнопки
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=i[1], callback_data=i[0]) for i in products
                    if i[2] > 0]
    # Добавляем кнопки в пространство
    kb.add(*all_products)
    kb.row(cart)
    return kb


# Кнопки выбора количества

def choose_pr_count_buttons(plus_or_minus='', min=1):
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(row_width=3)
    # создаем сами кнопки
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=min, callback_data=min)
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')

    if plus_or_minus == 'decrement':
        if min > 1:
            count = types.InlineKeyboardButton(text=str(min-1), callback=min)
    elif plus_or_minus == 'increment':
        count = types.InlineKeyboardButton(text=str(min+1), callback=min)

    kb.add(minus, count, plus)
    kb.row(to_cart, back)
    return kb


