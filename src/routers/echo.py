"""
Обработчик "Эхо", в данном случае реагирует на ввод текста с клавиатуры, не возвращает "эхо"
"""
from aiogram import Router, types

from keyboards.inline import get_callback_buttons

router = Router(name=__name__)


@router.message()
async def handle_echo(message: types.Message):
    """
    Обработка сообщений из чата (эхо)
    """
    text = f"What? 👀\nPress /start or read help page."
    await message.answer(
        text=text,
        reply_markup=get_callback_buttons(
            buttons={
                "📚 Help page": "help",
            },
            sizes=(2,),
        ),
    )
