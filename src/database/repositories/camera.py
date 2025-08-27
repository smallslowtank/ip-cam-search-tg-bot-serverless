from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from database.models.camera import Camera

from core.entities import CreateUser


class CameraRepository:

    def __init__(self, session: Session):
        self.session = session

    async def get_result(self, user: CreateUser) -> list:
        """
        запрос с фильтрами
        """

        # фильтры
        filters = []
        if user.search_camera_resolution == True:
            filters.append(
                Camera.camera_resolution == user.camera_resolution,
            )
        if user.search_camera_sensitivity_day_x10000 == True:
            filters.append(
                Camera.camera_sensitivity_day_x10000
                <= user.camera_sensitivity_day_x10000,
            )
        if user.search_camera_IR_illumination == True:
            filters.append(
                Camera.camera_IR_illumination >= user.camera_IR_illumination,
            )
        if user.search_camera_operating_temperature_min == True:
            filters.append(
                Camera.camera_operating_temperature_min
                <= user.camera_operating_temperature_min,
            )
        if user.search_camera_operating_temperature_max == True:
            filters.append(
                Camera.camera_operating_temperature_max
                >= user.camera_operating_temperature_max,
            )
        if user.search_camera_data_transfer_interface == True:
            filters.append(
                Camera.camera_data_transfer_interface.like(
                    f"%{user.camera_data_transfer_interface}%"
                ),
            )
        if user.search_camera_power_supply_poe == True:
            filters.append(
                Camera.camera_power_supply_poe == user.camera_power_supply_poe,
            )
        if user.search_camera_lightning_protection == True:
            filters.append(
                Camera.camera_lightning_protection == user.camera_lightning_protection,
            )
        if user.search_camera_comment == True:
            filters.append(
                Camera.camera_comment.like(
                    f"%{user.camera_comment}",
                ),
            )

        # запрос
        stmt = (
            select(
                Camera.camera_model,
            )
            .filter(
                and_(*filters),
            )
            .order_by(
                Camera.camera_model.asc(),
            )
        )
        res = await self.session.execute(stmt)
        result = res.scalars().all()
        if not result:
            return []
        return result


def camera_repository_factory(session):
    return CameraRepository(session)
