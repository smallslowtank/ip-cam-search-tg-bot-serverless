"""
Управление параметрами поиска
"""

from aiogram import Router, types, F

from core.services import user_service
from keyboards.inline import get_callback_buttons
from routers.base_commands import error_text
from routers.parameters_info import parameters_info

router = Router(name=__name__)


@router.callback_query(
    F.data == "camera_resolution",
)
async def camera_resolution_parameters_edit_callback(callback: types.CallbackQuery):
    """
    Команда "camera_resolution" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_resolution # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_resolution: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "разрешение" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: {parameter_value} Мп" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_resolution}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_resolution", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_resolution", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_sensitivity_day_x10000",
)
async def camera_sensitivity_day_x10000_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_sensitivity_day_x10000" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_sensitivity_day_x10000/10000 # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_sensitivity_day_x10000: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "чувствительность" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: от {parameter_value} лк и лучше" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_sensitivity_day_x10000}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_sensitivity_day_x10000", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_sensitivity_day_x10000", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_IR_illumination",
)
async def camera_IR_illumination_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_IR_illumination" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_IR_illumination # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_IR_illumination: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "ИК-подсветка" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: до {parameter_value} м или дальше" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_IR_illumination}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_IR_illumination", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_IR_illumination", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_operating_temperature_min",
)
async def camera_operating_temperature_min_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_operating_temperature_min" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_operating_temperature_min # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_operating_temperature_min: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "минимальная рабочая температура" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: до {parameter_value} °C или ниже" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_min}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_operating_temperature_min", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_min", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_operating_temperature_max",
)
async def camera_operating_temperature_max_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_operating_temperature_max" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_operating_temperature_max # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_operating_temperature_max: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "максимальная рабочая температура" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: до {parameter_value} °C или выше" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_max}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_operating_temperature_max", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_max", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_data_transfer_interface",
)
async def camera_data_transfer_interface_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_data_transfer_interface" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_data_transfer_interface # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_data_transfer_interface: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "сетевой интерфейс" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: {parameter_value}" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_data_transfer_interface}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать при поиске и задать значение": "set_camera_data_transfer_interface", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_data_transfer_interface", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_power_supply_poe",
)
async def camera_power_supply_poe_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_power_supply_poe" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_power_supply_poe # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_power_supply_poe: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "поддержка POE" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: есть" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_power_supply_poe}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать этот параметр при поиске": "set_camera_power_supply_poe", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_power_supply_poe", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_lightning_protection",
)
async def camera_lightning_protection_parameters_edit_callback(
    callback: types.CallbackQuery,
):
    """
    Команда "camera_lightning_protection" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_lightning_protection # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_lightning_protection: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "грозозащита" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: есть" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_lightning_protection}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать этот параметр при поиске": "set_camera_lightning_protection", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_lightning_protection", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "camera_comment",
)
async def camera_comment_parameters_edit_callback(callback: types.CallbackQuery):
    """
    Команда "camera_comment" (коллбэк)
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        parameter_value = user.camera_comment # Изменить
        parameter_search = "❌ Нет"
        if user.search_camera_comment: # Изменить
            parameter_search = "✅ Да"
        parameter_name = "комментарий" # Изменить
        text = f"Параметр: <b>{parameter_name}</b> \
            \nУчитывать при поиске: {parameter_search} \
            \nТекущее значение: {parameter_value}" # Изменить
        await callback.message.edit_text(text=text)
        await callback.message.answer(
            text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_comment}", # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "✅ Учитывать этот параметр при поиске": "set_camera_comment", # Изменить
                    "❌ Не учитывать этот параметр при поиске": "off_camera_comment", # Изменить
                    "📚 Help page": "help",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )
