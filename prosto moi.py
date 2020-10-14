import telebot
from telebot import types

ище = еудуище

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


@bot.message_handler(commands['/help'])
def command_help(m):
    cid = m.chat.id
    help_text = 'Доступны следующие команды \n'
    for key in commands:
        help_text += '/' + key ': '
        help_text += commands[key] + '\n'
        message(cid, help text, reply_markup=det_data_keyboard())

        help_text = ('Описание кнопки \n Кнопка "Сегодня" выводит расписание на сегодняшний день, '
                     'причем с учётной типа нидели (числитель/наменатель), но есть один нюанс: если сегоднявоскресенье'
                     'или время больше, чем 19:00, то выводится расписание на следующий день\n ')
        bot.send_message(cid, help_text, reply_markup=get_data_keyboard())
        guide_url = "@fuccbwoi"
        help_text = 'Более подробную инструкцию и помощь вы сможете узнать написав мне: {}'.format(guide_url)
        bot.send_message(cid, help_text, reply_markup=get_data_keyboard())
    bot.polling(none_stop=True)

