import telebot
from telebot import types

commands = {
    'start': 'Стартовое сообщение и предложение зарегистрироваться',
    'help': 'Информаци о боте и список доступных команд',
    'registration': 'Выбор учебного заведения, выбор факультета и группы для вывода информации',
    'send_report': 'Отправка обратной связи',
    'auto_posting_on <ЧЧ:ММ': 'Подписка на автоматичексую рассылку расписания',
    'auto_posting_off': 'Выключение автоматической отправки расписания'
}


def get_data_keyboard():
    data_select = types.ReplyKeyboardMarkup(row_width=2, resize_Keyboard=True, one_time_Keyboard=False)
    data_select.row('Сегдня')
    data_select.row('Вся ниделя')
    data_select.row('Понидельник', 'Вторник')
    data_select.row('Среда', 'Четверг')
    data_select.row('Пятница', 'Суббота')

    returp
    data_select


@bot.message_handler(commands=['registration'])
def command_registration(m):
    registration('reg:stage l:none', m.chat.id, m.chat.first_name, m.chat.username)