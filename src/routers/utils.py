"""
Вспомогательные функции
"""

from core.services import user_service, camera_service
from core.entities import CreateUser


async def create_list_of_cameras(user_id: int) -> str:
    """
    формирование списка камер
    """
    user = await user_service.get_by_id(user_id=user_id)
    list_cameras = await camera_service.get_result(user=user)
    result = ""
    count = 1
    for i in list_cameras:
        if i != "Список пуст":
            url_google = f'<a href="https://www.google.com/search?q={i}+ip+видеокамера">Google📖</a>'
            # url_yandex_market = f'<a href="https://market.yandex.ru/search?text={i}">Яндекс🛒</a>'
            url_yandex = (
                f'<a href="https://ya.ru/search?text={i}+ip+видеокамера">Яндекс🛒</a>'
            )
            result = f"{result}{str(count)}. {i} {url_google} {url_yandex}\n"
            count += 1
        else:
            result = i
    return result


async def create_list_of_parameters(user_id: int) -> str:
    """
    формирование списка параметров
    """
    user = await user_service.get_by_id(user_id=user_id)
    result = "✅ - учитывать параметр при поиске\n❌ - не учитывать параметр\n<b>Параметры поиска:</b>\n"
    if user.search_camera_resolution:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}Разрешение: {user.camera_resolution} Мп\n"
    if user.search_camera_sensitivity_day_x10000:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = (
        f"{result}Чувствительность: {user.camera_sensitivity_day_x10000/10000} лк или лучше\n"
    )
    if user.search_camera_IR_illumination:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}ИК-подсветка: {user.camera_IR_illumination} м или дальше\n"
    if user.search_camera_operating_temperature_min:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = (
        f"{result}Температура (min): {user.camera_operating_temperature_min} °C или ниже\n"
    )
    if user.search_camera_operating_temperature_max:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = (
        f"{result}Температура (max): {user.camera_operating_temperature_max} °C или выше\n"
    )
    if user.search_camera_data_transfer_interface:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}Сетевой интерфейс: {user.camera_data_transfer_interface}\n"
    if user.search_camera_power_supply_poe:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}Поддержка POE: Есть\n"
    if user.search_camera_lightning_protection:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}Грозозащита: Есть\n"
    if user.search_camera_comment:
        result = f"{result}✅"
    else:
        result = f"{result}❌"
    result = f"{result}Комментарий: {user.camera_comment}\n"
    return result


async def create_new_user(user_id: int) -> bool:
    try:
        new_user = CreateUser(
            user_id=user_id,
        )
        await user_service.add(user_info=new_user)
        return True
    except Exception as e:
        print("error:", e)
        return False
