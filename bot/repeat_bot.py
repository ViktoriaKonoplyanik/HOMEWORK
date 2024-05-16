
import telebot
from telebot import types

# Токен бота
bot_token = "6927164252:AAGfGukC5JecDGmZj_yhdKf1ypQWPd4WH1A"

# Идентификатор группы Telegram
group_id = -4214853093


# Класс чат-бота
class EchoBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

        @self.bot.message_handler(commands=['start'])
        def handle_commands(message):
            self.send_welcome(message)

        @self.bot.message_handler(content_types=['text'])
        def handle_messages(message):
            if message.text == "Оформить заявку":
                self.get_name(message)
            else:
                self.bot.send_message(message.chat.id, message.text)

    def send_welcome(self, message):
        self.bot.send_message(message.chat.id, "Привет! Я могу повторять за тобой,а также ты можешь попытать удачу и  оформить заявку на покупку автомобиля и если моя карьера в python сложиться благополучно, твоя  заявка вероятно будет рассмотрена! .")


        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text="Оформить заявку")
        keyboard.add(button)
        self.bot.send_message(message.chat.id, "Нажмите на кнопку ниже, чтобы оформить заявку:", reply_markup=keyboard)

    def get_name(self, message):
        self.bot.send_message(message.chat.id, "Введите ваше имя:")
        self.bot.register_next_step_handler(message, self.get_surname)

    def get_surname(self, message):
        self.name = message.text
        self.bot.send_message(message.chat.id, "Введите вашу фамилию:")
        self.bot.register_next_step_handler(message, self.get_car_make)

    def get_car_make(self, message):
        self.surname = message.text
        self.bot.send_message(message.chat.id, "Введите марку автомобиля, который вы хотели бы купить:")
        self.bot.register_next_step_handler(message, self.get_price)

    def get_price(self, message):
        self.car_make = message.text
        self.bot.send_message(message.chat.id, "Введите цену автомобиля в евро:")
        self.bot.register_next_step_handler(message, self.finalize_application)

    def finalize_application(self, message):
        price = message.text
        application_text = f"Заявка на покупку автомобиля:\n\n" \
                           f"Имя: {self.name}\n" \
                           f"Фамилия: {self.surname}\n" \
                           f"Марка автомобиля: {self.car_make}\n" \
                           f"Цена: {price}"

        self.bot.send_message(group_id, application_text)
        self.bot.send_message(message.chat.id, "Ваша заявка успешно отправлена!")

    def run(self):
        self.bot.polling()

# Запуск бота
if __name__ == '__main__':
    bot = EchoBot(bot_token)
    bot.run()


