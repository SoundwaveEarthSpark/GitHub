from itertools import product

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button5 = KeyboardButton(text='Купить')
kb.add(button1, button2, button5)

kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(button3, button4)

kb3 = InlineKeyboardMarkup()
p1 = InlineKeyboardButton(text='Кальций', callback_data='product_buying')
p2 = InlineKeyboardButton(text='Железо с витамином С', callback_data='product_buying')
p3 = InlineKeyboardButton(text='Йод', callback_data='product_buying')
p4 = InlineKeyboardButton(text='Магний с B6', callback_data='product_buying')
kb3.add(p1, p2, p3, p4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

product_all = get_all_products()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Выберите опцию:", reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in product_all:
        id, title, description, price = i
        with open(f'{id}.jpg', "rb") as img:
            await message.answer_photo(img,f"Название: {title} | Описание: {description} | Цена: {price}")
    await message.answer("Выберите продукт для покупки:", reply_markup = kb3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))
    calories = (10 * weight + 6.25 * growth - 5 * age - 161)
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
