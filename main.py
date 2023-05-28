import time
import pprint
import requests
from user import User
from bot_token import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     pprint.pprint(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# def say_something(number: int, word: str):
#     word = word.capitalize()
#     return word * number
#
#
# def get_user_info(user: User) -> str:
#     return f'Возраст пользователя {user.name} - {user.age}, ' \
#            f'а email - {user.email}'


# if __name__ == '__main__':
#     API_URL: str = 'https://api.telegram.org/bot'
#     API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
#     API_YES_NO_MAYBE: str = 'https://yesno.wtf/api'
#     ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
#     UPDATE_TEXT: str = ', вот ваша картинка)'
#     TEXT: str = 'Ура! Классный апдейт!'
#     MAX_COUNTER: int = 100
#     offset: int = -2
#     counter: int = 0
#     chat_id: int
#     cat_response: requests.Response
#     cat_link: str
#     ynm_response: requests.Response
#     ynm_link: str
#     user_name: str
#
#     while counter < 100:
#         print('attempt =', counter)
#         updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#         if updates['result']:
#             for result in updates['result']:
#                 offset = result['update_id']
#                 chat_id = result['message']['from']['id']
#                 user_name = result['message']['from']['first_name']
#                 ynm_response = requests.get(API_YES_NO_MAYBE)
#
#                 if ynm_response.status_code == 200:
#                     ynm_link = ynm_response.json()['image']
#                     # requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={user_name}{UPDATE_TEXT}')
#                     requests.get(f'{API_URL}{BOT_TOKEN}/sendAnimation?chat_id={chat_id}&animation={ynm_link}')
#                 else:
#                     requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#
#         time.sleep(1)
#         counter += 1

# print_hi('Julia')
# print(say_something(4, 'Julia'))
# user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
# print(get_user_info(user_1))
# api_url = 'http://jservice.io/api/random?count=1'
# api_url = 'http://yesno.wtf/api'
# api_url = 'https://api.telegram.org/bot6116391081:AAGKjm1LnbdcPmJoBtluLMocxOYEWTQlnU0/getUpdates'
# api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=265703213&text=Привет, Julia!'
#
# while True:
#     try:
#         response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
#         break
#     except:
#         time.sleep(5)
#
# if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#     pprint.pprint(response.text)
# else:
#     print(response.status_code)  # При другом коде ответа выводим этот код
