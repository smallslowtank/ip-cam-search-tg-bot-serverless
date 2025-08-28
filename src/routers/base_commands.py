"""
Обработчик базовых команд (start, help) и коллбэка help
"""

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f

from routers.utils import create_new_user
from keyboards.inline import get_callback_buttons
from core.services import user_service

router = Router(name=__name__)

start_page_text = "Это бот для подбора IP видеокамер. \
    \n📚 <b>Help page</b> - Инструкция по работе с ботом. \
    \n📝 <b>Main page</b> - Начать работу с ботом."

help_page_text = """📚 Help page. \
\nЭто телеграм-бот для подбора IP-видеокамер. \
\n\nВ текущей версии бота доступен только поиск по параметрам, которые нужно задать вручную. \
\nИнформация, которую предоставляет бот, несёт ознакомительный характер, \
точные характеристики или цену камеры следует уточнять у производителя (продавца). \
\n\nДля удобства в ответе бота есть ссылки на поисковые запросы по модели камеры. \
Ссылки будут активны только для первых 50 моделей в ответе. \
\n\nПри выборе параметров следует учесть что: \
\n- Если параметр отмечен знаком ❌, то этот параметр не учитывается при поиске. \
\n- Параметр "Разрешение" подразумевает, что будут найдены камеры только с выбранным значением разрешения. \
Единица измерения: мегапиксель. \
\n- Параметр "Чувствительность" подразумевает, что будут найдены камеры с таким или лучшим значением. \
Для видеокамер - чем меньше значение, тем лучше. Единица измерения: люкс. \
\n- Параметр "ИК-подсветка" подразумевает, что будут найдены камеры с таким или \
лучшим (большим) значением дальности ИК-подсветки. Единица измерения: метр. \
\n- Параметр "Минимальная рабочая температура" подразумевает, \
что будут найдены камеры с таким или лучшим (ниже) значением. Единица измерения: градус Цельсия. \
\n- Параметр "Максимальная рабочая температура" подразумевает, \
что будут найдены камеры с таким или лучшим (выше) значением. Единица измерения: градус Цельсия. \
\n- Параметр "Сетевой интерфейс" подразумевает, что будут найдены камеры, имеющие такой тип интерфейса. \
\n- Параметр "Поддержка POE" подразумевает, что будут найдены камеры, поддерживающие POE. \
\n- Параметр "Грозозащита" подразумевает, что будут найдены камеры, имеющие грозозащиту. \
\n- Параметр "Комментарий" в текущей версии поддерживает поиск камер, \
имеющих Сертификат по Постановлению Правительства № 969. \
\n\nБот написан на Python и использует serverless-технологии Яндекс Облака."""

error_text = "Error\nPress /start"


@router.message(
    or_f(
        CommandStart(),
        F.text.lower() == "start",
        F.text.lower() == "старт",
    )
)
async def start_command(message: types.Message):
    """
    Команда "старт"
    """
    await message.react(reaction=[{"type": "emoji", "emoji": "🔥"}])
    try:
        user_id = message.from_user.id
        if await user_service.check_by_id(user_id=user_id) == False:
            await create_new_user(user_id=user_id)
        await message.answer(
            text=start_page_text,
            reply_markup=get_callback_buttons(
                buttons={
                    "📚 Help page": "help",
                    "📝 Main page": "main",
                },
                sizes=(2,),
            ),
        )
    except Exception as e:
        print("error:", e)
        await message.answer(
            text=error_text,
        )


@router.message(
    or_f(
        Command("help"),
        F.text.lower() == "help",
    )
)
async def help_command(message: types.Message):
    """
    Команда "help"
    """
    await message.react(reaction=[{"type": "emoji", "emoji": "👀"}])
    try:
        user_id = message.from_user.id
        if await user_service.check_by_id(user_id=user_id) == False:
            await create_new_user(user_id=user_id)
        user_id_text = f"\nYou Telegram ID: {user_id}"
        await message.answer(
            text=help_page_text + user_id_text,
            reply_markup=get_callback_buttons(
                buttons={
                    "📝 Main page": "main",
                },
                sizes=(1,),
            ),
        )
    except Exception as e:
        print("error:", e)
        await message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "help",
)
async def help_callback(callback: types.CallbackQuery):
    """
    Команда "help" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user_id_text = f"\nYou Telegram ID: {user_id}"
        await callback.message.edit_text(
            text=help_page_text + user_id_text,
            reply_markup=get_callback_buttons(
                buttons={
                    "📝 Main page": "main",
                },
                sizes=(1,),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )
