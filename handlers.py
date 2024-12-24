from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
import keyboard as kb
import chatgpt as gpt

router = Router()

class request_code(StatesGroup):
    request = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "🤖Приветствую, я бот - помощник RKSI, который может помочь тебе с составлением или объяснением кода, а также я умею генерировать картинки🤖",
        reply_markup=kb.main
    )

@router.message(F.text == 'Что я умею? 📋')
async def get_info(message: Message):
	await message.answer(" 🤖Что умеет данный бот?🤖 \n1.Генерация кода💻 \n2.Объяснение кода🧠 \n3.Переход на сайт твоего колледжа☠",
                         reply_markup=kb.get_info)

@router.message(F.text == 'Сайт ☠')
async def website(message: Message):
    await message.answer("Ссылка: [https://rksi.ru/](https://rksi.ru/)",
                         parse_mode="Markdown",
                         reply_markup=kb.website)

@router.message(F.text == 'Код 🧠')
async def code(message: Message, state: FSMContext):
    await message.reply("Вы выбрали режим редактирования и объяснения кода🦾 "
                        "Если хотите выйти из этого режима - нажмите кнопку",
                        reply_markup=kb.cancel)
    await state.set_state(request_code.request)

@router.message(request_code.request)
async def code_answer(message: Message, state: FSMContext):
    await message.reply(gpt.answer_code(message.text),
                        reply_markup=kb.cancel)
    await state.clear()
    await state.set_state(request_code.request)
    await message.answer("Напишите ещё запросы:")

@router.callback_query(F.data == "cancel")
async def callback_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Вы вышли из режима редактирования кода!")
    await callback.answer()

@router.callback_query(F.data == "website")
async def callback_website(callback: CallbackQuery):
    await callback.message.answer("Ссылка: [https://rksi.ru/](https://rksi.ru/)",
                         parse_mode="Markdown",
                         reply_markup=kb.website)
    await callback.answer()

@router.callback_query(F.data == "code")
async def callback_code(callback: CallbackQuery, state: FSMContext):
    await callback.message.reply("Вы выбрали режим редактирования и объяснения кода🦾 "
                        "Если хотите выйти из этого режима - нажмите кнопку",
                        reply_markup=kb.cancel)
    await state.set_state(request_code.request)
    await callback.answer()
