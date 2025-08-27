"""
Исключение параметров из поиска
"""

from aiogram import Router, types, F

from core.services import user_service
from keyboards.inline import get_callback_buttons
from routers.base_commands import error_text
from routers.parameters_info import parameters_info

router = Router(name=__name__)


@router.callback_query(
    F.data == "off_camera_resolution", # Изменить
)
async def off_camera_resolution_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_resolution" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_resolution: # Изменить
            user.search_camera_resolution = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_resolution}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_resolution", # Изменить
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
    F.data == "off_camera_sensitivity_day_x10000", # Изменить
)
async def off_camera_sensitivity_day_x10000_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_sensitivity_day_x10000" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_sensitivity_day_x10000: # Изменить
            user.search_camera_sensitivity_day_x10000 = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_sensitivity_day_x10000}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_sensitivity_day_x10000", # Изменить
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
    F.data == "off_camera_IR_illumination", # Изменить
)
async def off_camera_IR_illumination_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_IR_illumination" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_IR_illumination: # Изменить
            user.search_camera_IR_illumination = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_IR_illumination}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_IR_illumination", # Изменить
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
    F.data == "off_camera_operating_temperature_min", # Изменить
)
async def off_camera_operating_temperature_min_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_operating_temperature_min" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_operating_temperature_min: # Изменить
            user.search_camera_operating_temperature_min = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_min}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_operating_temperature_min", # Изменить
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
    F.data == "off_camera_operating_temperature_max", # Изменить
)
async def off_camera_operating_temperature_max_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_operating_temperature_max" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_operating_temperature_max: # Изменить
            user.search_camera_operating_temperature_max = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_max}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_operating_temperature_max", # Изменить
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
    F.data == "off_camera_data_transfer_interface", # Изменить
)
async def off_camera_data_transfer_interface_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_data_transfer_interface" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_data_transfer_interface: # Изменить
            user.search_camera_data_transfer_interface = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_data_transfer_interface}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_data_transfer_interface", # Изменить
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
    F.data == "off_camera_power_supply_poe", # Изменить
)
async def off_camera_power_supply_poe_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_power_supply_poe" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_power_supply_poe: # Изменить
            user.search_camera_power_supply_poe = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_power_supply_poe}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_power_supply_poe", # Изменить
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
    F.data == "off_camera_lightning_protection", # Изменить
)
async def off_camera_lightning_protection_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_lightning_protection" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_lightning_protection: # Изменить
            user.search_camera_lightning_protection = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_lightning_protection}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_lightning_protection", # Изменить
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
    F.data == "off_camera_comment", # Изменить
)
async def off_camera_comment_callback(callback: types.CallbackQuery): # Изменить
    """
    Команда "off_camera_comment" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_comment: # Изменить
            user.search_camera_comment = False # Изменить
            if await user_service.update(user=user):
                await callback.message.edit_text(
                    text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_comment}\n❌ Параметр исключен из поискового запроса", # Изменить
                )
                await callback.message.answer(
                    text="Этот параметр не будет влиять на результаты поиска.",
                    reply_markup=get_callback_buttons(
                        buttons={
                            "🔎 Найти": "search",
                            "🛠 Другие параметры": "parameters_edit",
                            "✅ Учитывать при поиске и задать значение": "set_camera_comment", # Изменить
                        },
                        sizes=(2,),
                    ),
                )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )
