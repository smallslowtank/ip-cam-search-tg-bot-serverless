__all__ = ("router",)

from aiogram import F, Router

from .base_commands import router as base_commands_router
from .business_base import router as business_router
from .business_edit_parameters import router as business_edit_parameters_router
from .business_off_parameters import router as business_off_parameters_router
from .business_set_parameters import router as business_set_parameters_router
from .echo import router as echo_router

router = Router(name=__name__)

# фильтры для сообщений
router.message.filter(
    F.chat.type == "private",
)

router.include_routers(
    base_commands_router,
    business_router,
    business_edit_parameters_router,
    business_off_parameters_router,
    business_set_parameters_router,
    # Эхо-роутер должен быть подключен последним
    echo_router,
)
