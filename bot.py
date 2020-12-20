import telebot
from telebot import types
import config

bot = telebot.TeleBot('1489724692:AAHJVhE-0C3G69eSG5RWiUovVgyZYcuLW9c')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Жанры')
    btn2 = types.KeyboardButton('Популярное')
    btn3 = types.KeyboardButton("Новинки")
    btn4 = types.KeyboardButton("Рекомендации")
    btn5 = types.KeyboardButton("Аудиокниги")
    btn6 = types.KeyboardButton("Что почитать?")
    btn7 = types.KeyboardButton("Мой Рекомендации")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    send_mess = f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот для книжного сайта www.litres.ru"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == 'Жанры':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Жанры нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    elif message.text == 'Популярное':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/luchshie-knigi/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Популярное нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    elif message.text == 'Новинки':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/novie/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Новинки нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    elif message.text == 'Рекомендации':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/recommend/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Рекомендации нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    elif message.text == 'Аудиокниги':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/chto-slushat/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Аудиокниги нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    elif message.text == 'Что почитать?':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.litres.ru/chto-chitat/")
        keyboard.add(url_btn1)
        bot.send_message(message.chat.id, "Чтобы перейти на раздел Что почитать? нажмите на кнопку ниже", parse_mode="html", reply_markup=keyboard)
    if message.text == 'Мой Рекомендации':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Парфюмер. История одного убийцы - Патрик Зюскинд", url="https://www.litres.ru/patrik-zuskind/parfumer-istoriya-odnogo-ubiycy-56282860/")
        url_btn2 = types.InlineKeyboardButton(text="Властелин Колец - Джон Роналд Руэл Толкин", url="https://www.litres.ru/dzhon-tolkin/vlastelin-kolec/")
        url_btn3 = types.InlineKeyboardButton(text="1984 - Джордж Оруэлл", url="https://www.litres.ru/dzhordzh-oruell/1984/")
        url_btn4 = types.InlineKeyboardButton(text="Самурай без меча - Китами Масао", url="https://www.litres.ru/kitami-masao/samuray-bez-mecha/")
        url_btn5 = types.InlineKeyboardButton(text="Кайдзен. Ключ к успеху японских компаний - Масааки Имаи", url="https://www.litres.ru/imai-masaaki/kaydzen-kluch-k-uspehu-yaponskih-kompaniy-17503286/")
        url_btn6 = types.InlineKeyboardButton(text="Sapiens. Краткая история человечества - Юваль Ной Харари", url="https://www.litres.ru/uval-noy-harari/sapiens-kratkaya-istoriya-chelovechestva/")
        keyboard.add(url_btn1, url_btn2, url_btn3, url_btn4, url_btn5, url_btn6)
        bot.send_message(message.chat.id, "Здесь собраны Мой Рекомендации", parse_mode="html", reply_markup=keyboard)

bot.polling(none_stop=True)