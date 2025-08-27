from sqlalchemy import Integer, Column, String, Boolean

from database.base import Base


class User(Base):
    __tablename__ = "users"

    # Идентификатор пользователя
    user_id = Column(Integer, primary_key=True)

    # Параметры камеры для поиска
    camera_resolution = Column(Integer, nullable=False)
    camera_sensitivity_day_x10000 = Column(Integer, nullable=False)
    camera_IR_illumination = Column(Integer, nullable=False)
    camera_operating_temperature_min = Column(Integer, nullable=False)
    camera_operating_temperature_max = Column(Integer, nullable=False)
    camera_data_transfer_interface = Column(String, nullable=False)
    camera_power_supply_poe = Column(Boolean, nullable=False)
    camera_lightning_protection = Column(Boolean, nullable=False)
    camera_comment = Column(String, nullable=False)

    # Какие параметры камеры включить в поисковый запрос
    search_camera_resolution = Column(Boolean, nullable=False)
    search_camera_sensitivity_day_x10000 = Column(Boolean, nullable=False)
    search_camera_IR_illumination = Column(Boolean, nullable=False)
    search_camera_operating_temperature_min = Column(Boolean, nullable=False)
    search_camera_operating_temperature_max = Column(Boolean, nullable=False)
    search_camera_data_transfer_interface = Column(Boolean, nullable=False)
    search_camera_power_supply_poe = Column(Boolean, nullable=False)
    search_camera_lightning_protection = Column(Boolean, nullable=False)
    search_camera_comment = Column(Boolean, nullable=False)
