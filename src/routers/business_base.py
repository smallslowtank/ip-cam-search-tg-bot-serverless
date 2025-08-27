"""
Обработчик бизнес логики
"""

from aiogram import Router, types, F

from keyboards.inline import get_callback_buttons
from routers.utils import create_list_of_cameras, create_list_of_parameters
from routers.base_commands import error_text

router = Router(name=__name__)

main_page_text = "📝 Main page. Главная страница.\nКакой тип поиска использовать?"
search_page_text = "Предыдущие сообщения содержат параметры поиска и список камер."


@router.callback_query(
    F.data == "main",
)
async def main_callback(callback: types.CallbackQuery):
    """
    Команда "main" (коллбэк)
    """
    await callback.message.edit_text(
        text=main_page_text,
        reply_markup=get_callback_buttons(
            buttons={
                "🤖 Интеллектуальный поиск": "search_ai",
                "👍 Поиск по параметрам": "search_by_parameters",
                "📚 Help page": "help",
            },
            sizes=(1,),
        ),
    )


@router.callback_query(
    F.data == "search_by_parameters",
)
async def search_by_parameters_callback(callback: types.CallbackQuery):
    """
    Команда "search_by_parameters" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        list_parameters_search_page_text = await create_list_of_parameters(
            user_id=user_id
        )
        await callback.message.edit_text(
            text=list_parameters_search_page_text,
            reply_markup=get_callback_buttons(
                buttons={
                    "📚 Help page": "help",
                    "📝 Main page": "main",
                    "🛠 Изменить параметры": "parameters_edit",
                    "🔎 Найти": "search",
                },
                sizes=(2,2,),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "search",
)
async def search_callback(callback: types.CallbackQuery):
    """
    Команда "search" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        list_parameters_search_page_text = await create_list_of_parameters(
            user_id=user_id
        )
        await callback.message.edit_text(
            text=f"{list_parameters_search_page_text}\n<b>Результаты поиска:</b>",
        )
        list_cameras_search_page_text = await create_list_of_cameras(user_id=user_id)
        await callback.message.answer(
            text=list_cameras_search_page_text,
        )
        await callback.message.answer(
            text=search_page_text,
            reply_markup=get_callback_buttons(
                buttons={
                    "📚 Help page": "help",
                    "📝 Main page": "main",
                    "🛠 Изменить параметры": "parameters_edit",
                },
                sizes=(2,),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "search_ai",
)
async def search_ai_callback(callback: types.CallbackQuery):
    """
    Команда "search_ai" (коллбэк)
    """
    await callback.message.edit_text(
        text="🤖 Интеллектуальный поиск в разработке.",
        reply_markup=get_callback_buttons(
            buttons={
                "📚 Help page": "help",
                "📝 Main page": "main",
                "👍 Поиск по параметрам": "search_by_parameters",
            },
            sizes=(2,),
        ),
    )


@router.callback_query(
    F.data == "parameters_edit",
)
async def parameters_edit_callback(callback: types.CallbackQuery):
    """
    Команда "parameters_edit" (коллбэк)
    """
    user_id = callback.from_user.id
    list_parameters_search_page_text = await create_list_of_parameters(
        user_id=user_id
    )
    await callback.message.edit_text(
        text=f"{list_parameters_search_page_text}\n🛠 <b>Какой параметр поиска изменить?</b>",
        reply_markup=get_callback_buttons(
            buttons={
                "📝 Main page": "main",
                "🔎 Найти": "search",
                "Разрешение": "camera_resolution",
                "Чувствительность": "camera_sensitivity_day_x10000",
                "ИК-подсветка": "camera_IR_illumination",
                "Температура (min)": "camera_operating_temperature_min",
                "Температура (max)": "camera_operating_temperature_max",
                "Сетевой интерфейс": "camera_data_transfer_interface",
                "Поддержка POE": "camera_power_supply_poe",
                "Грозозащита": "camera_lightning_protection",
                "Комментарий": "camera_comment",
            },
            sizes=(2,),
        ),
    )
