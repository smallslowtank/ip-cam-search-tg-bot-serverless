from sqlalchemy import select, update
from sqlalchemy.orm import Session

from core.entities import CreateUser
from database.models.user import User


class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    async def get_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.user_id == user_id)
        res = await self.session.execute(stmt)
        result = res.scalars().first()
        return result

    async def add(self, user_info: CreateUser) -> bool:
        try:
            self.session.add(
                User(
                    user_id=user_info.user_id,
                    camera_resolution=user_info.camera_resolution,
                    camera_sensitivity_day_x10000=user_info.camera_sensitivity_day_x10000,
                    camera_IR_illumination=user_info.camera_IR_illumination,
                    camera_operating_temperature_min=user_info.camera_operating_temperature_min,
                    camera_operating_temperature_max=user_info.camera_operating_temperature_max,
                    camera_data_transfer_interface=user_info.camera_data_transfer_interface,
                    camera_power_supply_poe=user_info.camera_power_supply_poe,
                    camera_lightning_protection=user_info.camera_lightning_protection,
                    camera_comment=user_info.camera_comment,
                    search_camera_resolution=user_info.search_camera_resolution,
                    search_camera_sensitivity_day_x10000=user_info.search_camera_sensitivity_day_x10000,
                    search_camera_IR_illumination=user_info.search_camera_IR_illumination,
                    search_camera_operating_temperature_min=user_info.search_camera_operating_temperature_min,
                    search_camera_operating_temperature_max=user_info.search_camera_operating_temperature_max,
                    search_camera_data_transfer_interface=user_info.search_camera_data_transfer_interface,
                    search_camera_power_supply_poe=user_info.search_camera_power_supply_poe,
                    search_camera_lightning_protection=user_info.search_camera_lightning_protection,
                    search_camera_comment=user_info.search_camera_comment,
                )
            )
            return True
        except:
            return False

    async def update(self, user_info: CreateUser) -> bool:
        try:
            stmt = (
                update(User)
                .where(User.user_id == user_info.user_id)
                .values(
                    camera_resolution=user_info.camera_resolution,
                    camera_sensitivity_day_x10000=user_info.camera_sensitivity_day_x10000,
                    camera_IR_illumination=user_info.camera_IR_illumination,
                    camera_operating_temperature_min=user_info.camera_operating_temperature_min,
                    camera_operating_temperature_max=user_info.camera_operating_temperature_max,
                    camera_data_transfer_interface=user_info.camera_data_transfer_interface,
                    camera_power_supply_poe=user_info.camera_power_supply_poe,
                    camera_lightning_protection=user_info.camera_lightning_protection,
                    camera_comment=user_info.camera_comment,
                    search_camera_resolution=user_info.search_camera_resolution,
                    search_camera_sensitivity_day_x10000=user_info.search_camera_sensitivity_day_x10000,
                    search_camera_IR_illumination=user_info.search_camera_IR_illumination,
                    search_camera_operating_temperature_min=user_info.search_camera_operating_temperature_min,
                    search_camera_operating_temperature_max=user_info.search_camera_operating_temperature_max,
                    search_camera_data_transfer_interface=user_info.search_camera_data_transfer_interface,
                    search_camera_power_supply_poe=user_info.search_camera_power_supply_poe,
                    search_camera_lightning_protection=user_info.search_camera_lightning_protection,
                    search_camera_comment=user_info.search_camera_comment,
                )
            )
            await self.session.execute(stmt)
            return True
        except Exception as e:
            print("error:", e)
            return False


def user_repository_factory(session):
    return UserRepository(session)
