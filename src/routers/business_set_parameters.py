"""
Включение параметров в поиск и выбор их значений
"""

from aiogram import Router, types, F

from core.services import user_service
from keyboards.inline import get_callback_buttons
from routers.base_commands import error_text
from routers.parameters_info import parameters_info

router = Router(name=__name__)


@router.callback_query(
    F.data == "set_camera_resolution",  # Изменить
)
async def set_camera_resolution_callback(callback: types.CallbackQuery):  # Изменить
    """
    Команда "set_camera_resolution" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_resolution == False:  # Изменить
            user.search_camera_resolution = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_resolution}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_resolution} Мп\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "2 Мп": "set_camera_resolution_2",
                    "4 Мп": "set_camera_resolution_4",
                    "5 Мп": "set_camera_resolution_5",
                    "8 Мп": "set_camera_resolution_8",
                    "10 Мп": "set_camera_resolution_10",
                    "12 Мп": "set_camera_resolution_12",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_resolution",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(3, 3, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_resolution_"),  # Изменить
)
async def set_camera_resolution_N_callback(callback: types.CallbackQuery):  # Изменить
    """
    Команда "set_camera_resolution_N" (коллбэк) # Изменить
    """
    try:
        value = int(callback.data.split("_")[3])  # Изменить
        if value in (2, 4, 5, 8, 10, 12):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_resolution != value:  # Изменить
                user.camera_resolution = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_resolution} Мп\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "2 Мп": "set_camera_resolution_2",
                                "4 Мп": "set_camera_resolution_4",
                                "5 Мп": "set_camera_resolution_5",
                                "8 Мп": "set_camera_resolution_8",
                                "10 Мп": "set_camera_resolution_10",
                                "12 Мп": "set_camera_resolution_12",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_resolution",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(3, 3, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_sensitivity_day_x10000",  # Изменить
)
async def set_camera_sensitivity_day_x10000_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_sensitivity_day_x10000" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_sensitivity_day_x10000 == False:  # Изменить
            user.search_camera_sensitivity_day_x10000 = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_sensitivity_day_x10000}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_sensitivity_day_x10000/10000} лк\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "от 0.1 лк": "set_camera_sensitivity_day_x10000_1000",
                    "от 0.01 лк": "set_camera_sensitivity_day_x10000_100",
                    "от 0.001 лк": "set_camera_sensitivity_day_x10000_10",
                    "от 0.0001 лк": "set_camera_sensitivity_day_x10000_1",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_sensitivity_day_x10000",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(2, 2, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_sensitivity_day_x10000_"),  # Изменить
)
async def set_camera_sensitivity_day_x10000_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_sensitivity_day_x10000_N" (коллбэк) # Изменить
    """
    try:
        value = int(callback.data.split("_")[5])
        if value in (1, 10, 100, 1000):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_sensitivity_day_x10000 != value:  # Изменить
                user.camera_sensitivity_day_x10000 = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_sensitivity_day_x10000/10000} лк\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "от 0.1 лк": "set_camera_sensitivity_day_x10000_1000",
                                "от 0.01 лк": "set_camera_sensitivity_day_x10000_100",
                                "от 0.001 лк": "set_camera_sensitivity_day_x10000_10",
                                "от 0.0001 лк": "set_camera_sensitivity_day_x10000_1",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_sensitivity_day_x10000",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(2, 2, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_IR_illumination",  # Изменить
)
async def set_camera_IR_illumination_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_IR_illumination" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_IR_illumination == False:  # Изменить
            user.search_camera_IR_illumination = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_IR_illumination}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_IR_illumination} м или больше\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "10 м": "set_camera_IR_illumination_10",
                    "30 м": "set_camera_IR_illumination_30",
                    "50 м": "set_camera_IR_illumination_50",
                    "100 м": "set_camera_IR_illumination_100",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_IR_illumination",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(4, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_IR_illumination_"),  # Изменить
)
async def set_camera_IR_illumination_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_IR_illumination_N" (коллбэк) # Изменить
    """
    try:
        value = int(callback.data.split("_")[4])
        if value in (10, 30, 50, 100):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_IR_illumination != value:  # Изменить
                user.camera_IR_illumination = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_IR_illumination} м или больше\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "10 м": "set_camera_IR_illumination_10",
                                "30 м": "set_camera_IR_illumination_30",
                                "50 м": "set_camera_IR_illumination_50",
                                "100 м": "set_camera_IR_illumination_100",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_IR_illumination",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(4, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_operating_temperature_min",  # Изменить
)
async def set_camera_operating_temperature_min_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_operating_temperature_min" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_operating_temperature_min == False:  # Изменить
            user.search_camera_operating_temperature_min = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_min}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_operating_temperature_min} °C или ниже\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "-10 °C": "set_camera_operating_temperature_min_-10",
                    "-20 °C": "set_camera_operating_temperature_min_-20",
                    "-30 °C": "set_camera_operating_temperature_min_-30",
                    "-40 °C": "set_camera_operating_temperature_min_-40",
                    "-50 °C": "set_camera_operating_temperature_min_-50",
                    "-60 °C": "set_camera_operating_temperature_min_-60",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_min",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(3, 3, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_operating_temperature_min_"),  # Изменить
)
async def set_camera_operating_temperature_min_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_operating_temperature_min_N" (коллбэк) # Изменить
    """
    try:
        value = int(callback.data.split("_")[5])  # Изменить
        if value in (-10, -20, -30, -40, -50, -60):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_operating_temperature_min != value:  # Изменить
                user.camera_operating_temperature_min = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_operating_temperature_min} °C или ниже\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "-10 °C": "set_camera_operating_temperature_min_-10",
                                "-20 °C": "set_camera_operating_temperature_min_-20",
                                "-30 °C": "set_camera_operating_temperature_min_-30",
                                "-40 °C": "set_camera_operating_temperature_min_-40",
                                "-50 °C": "set_camera_operating_temperature_min_-50",
                                "-60 °C": "set_camera_operating_temperature_min_-60",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_min",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(3, 3, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_operating_temperature_max",  # Изменить
)
async def set_camera_operating_temperature_max_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_operating_temperature_max" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_operating_temperature_max == False:  # Изменить
            user.search_camera_operating_temperature_max = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_operating_temperature_max}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_operating_temperature_max} °C или выше\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "30 °C": "set_camera_operating_temperature_max_30",
                    "40 °C": "set_camera_operating_temperature_max_40",
                    "50 °C": "set_camera_operating_temperature_max_50",
                    "60 °C": "set_camera_operating_temperature_max_60",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_max",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(4, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_operating_temperature_max_"),  # Изменить
)
async def set_camera_operating_temperature_max_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_operating_temperature_max_N" (коллбэк) # Изменить
    """
    try:
        value = int(callback.data.split("_")[5])  # Изменить
        if value in (30, 40, 50, 60):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_operating_temperature_max != value:  # Изменить
                user.camera_operating_temperature_max = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_operating_temperature_max} °C или выше\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "30 °C": "set_camera_operating_temperature_max_30",
                                "40 °C": "set_camera_operating_temperature_max_40",
                                "50 °C": "set_camera_operating_temperature_max_50",
                                "60 °C": "set_camera_operating_temperature_max_60",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_operating_temperature_max",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(4, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_data_transfer_interface",  # Изменить
)
async def set_camera_data_transfer_interface_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_data_transfer_interface" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_data_transfer_interface == False:  # Изменить
            user.search_camera_data_transfer_interface = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_data_transfer_interface}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_data_transfer_interface}\nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "RJ45": "set_camera_data_transfer_interface_RJ45",
                    # "BNC": "set_camera_data_transfer_interface_BNC",
                    # "RS-485": "set_camera_data_transfer_interface_RS-485",
                    # "SFP": "set_camera_data_transfer_interface_SFP",
                    "Wi-Fi": "set_camera_data_transfer_interface_Wi-Fi",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_data_transfer_interface",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(2, 1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data.startswith("set_camera_data_transfer_interface_"),  # Изменить
)
async def set_camera_data_transfer_interface_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_data_transfer_interface_N" (коллбэк) # Изменить
    """
    try:
        value = callback.data.split("_")[5]  # Изменить
        if value in ("RJ45", "BNC", "RS-485", "SFP", "Wi-Fi"):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_data_transfer_interface != value:  # Изменить
                user.camera_data_transfer_interface = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_data_transfer_interface}\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "RJ45": "set_camera_data_transfer_interface_RJ45",
                                # "BNC": "set_camera_data_transfer_interface_BNC",
                                # "RS-485": "set_camera_data_transfer_interface_RS-485",
                                # "SFP": "set_camera_data_transfer_interface_SFP",
                                "Wi-Fi": "set_camera_data_transfer_interface_Wi-Fi",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_data_transfer_interface",  # Изменить
                                "🔎 Найти": "search",
                                "🛠 Другие параметры": "parameters_edit",
                            },
                            sizes=(2, 1, 2),
                        ),
                    )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_power_supply_poe",  # Изменить
)
async def set_camera_power_supply_poe_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_power_supply_poe" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_power_supply_poe == False:  # Изменить
            user.search_camera_power_supply_poe = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_power_supply_poe}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: есть",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "❌ Не учитывать этот параметр при поиске": "off_camera_power_supply_poe",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_lightning_protection",  # Изменить
)
async def set_camera_lightning_protection_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_lightning_protection" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_lightning_protection == False:  # Изменить
            user.search_camera_lightning_protection = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_lightning_protection}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: есть",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "❌ Не учитывать этот параметр при поиске": "off_camera_lightning_protection",  # Изменить
                    "🔎 Найти": "search",
                    "🛠 Другие параметры": "parameters_edit",
                },
                sizes=(1, 2),
            ),
        )
    except Exception as e:
        print("error:", e)
        await callback.message.answer(
            text=error_text,
        )


@router.callback_query(
    F.data == "set_camera_comment",  # Изменить
)
async def set_camera_comment_callback(callback: types.CallbackQuery):  # Изменить
    """
    Команда "set_camera_comment" (коллбэк) # Изменить
    """
    try:
        user_id = callback.from_user.id
        user = await user_service.get_by_id(user_id=user_id)
        if user.search_camera_comment == False:  # Изменить
            user.search_camera_comment = True  # Изменить
            await user_service.update(user=user)
            await callback.message.edit_text(
                text=f"ℹ️ <u>Справка:</u> {parameters_info.info_camera_comment}\n✅ Параметр включен в поисковый запрос"  # Изменить
            )
        else:
            await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(
            text=f"Значение: {user.camera_comment} \nИзменить?",  # Изменить
            reply_markup=get_callback_buttons(
                buttons={
                    "969": "set_camera_comment_969",
                    "❌ Не учитывать этот параметр при поиске": "off_camera_comment",  # Изменить
                    "🔎 Найти": "search",
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
    F.data.startswith("set_camera_comment_"),  # Изменить
)
async def set_camera_comment_N_callback(
    callback: types.CallbackQuery,
):  # Изменить
    """
    Команда "set_camera_comment_N" (коллбэк) # Изменить
    """
    try:
        value = callback.data.split("_")[3]  # Изменить
        if value in ("969"):  # Изменить
            user_id = callback.from_user.id
            user = await user_service.get_by_id(user_id=user_id)
            if user.camera_comment != value:  # Изменить
                user.camera_comment = value  # Изменить
                if await user_service.update(user=user):
                    await callback.message.edit_text(
                        text=f"✅ Параметр изменён\nЗначение: {user.camera_comment}\nИзменить?",  # Изменить
                        reply_markup=get_callback_buttons(
                            buttons={
                                "969": "set_camera_comment_969",
                                "❌ Не учитывать этот параметр при поиске": "off_camera_comment",  # Изменить
                                "🔎 Найти": "search",
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
