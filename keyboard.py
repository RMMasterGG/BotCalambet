from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Что я умею? 📋')],
        [KeyboardButton(text='Сайт ☠'), KeyboardButton(text='Код 🧠')]
    ],
    resize_keyboard=True, 
    input_field_placeholder='👾Выберите свою цель👾'
)


get_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Преподаватели 👩🏻‍🏫", callback_data="teachers"), InlineKeyboardButton(text="Код 🧠", callback_data="code")]
])

website = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Нажми на меня", url="https://rksi.ru/")]])

cancel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="cancel")]])