from sqlalchemy import Integer, Column, String, Boolean

from database.base import Base


class Camera(Base):
    __tablename__ = "cameras"

    # Идентификатор и модель камеры, не должны быть пустыми
    camera_id = Column(Integer, primary_key=True)
    camera_model = Column(String, nullable=False)

    # Сырые параметры кармеры (не для поиска по параметрам)
    camera_sensitivity_raw = Column(String, nullable=True)
    camera_operating_temperature_raw = Column(String, nullable=True)
    camera_resolution_raw = Column(String, nullable=True)
    camera_lens_type = Column(String, nullable=True)
    camera_power_raw = Column(String, nullable=True)

    # Сырые параметры кармеры
    # (возможен поиск по спец запросу
    # или извлечение значений для стандартного поиска)
    camera_compression_codec = Column(String, nullable=True)
    camera_memory_card_support = Column(String, nullable=True)
    camera_audio_inputs_outputs = Column(String, nullable=True)
    camera_alarm_inputs_outputs = Column(String, nullable=True)
    camera_SATA_quantity_capacity = Column(String, nullable=True)
    camera_independent_video_outputs = Column(String, nullable=True)
    camera_data_transfer_rate = Column(String, nullable=True)
    camera_power_supply_raw = Column(String, nullable=True)
    camera_case_type = Column(String, nullable=True)
    camera_power_x10 = Column(Integer, nullable=True)
    
    # Параметры камеры для стандартного поиска по параметрам
    camera_IR_illumination = Column(Integer, nullable=True)
    camera_lightning_protection = Column(Boolean, nullable=True)
    camera_comment = Column(String, nullable=True)
    camera_data_transfer_interface = Column(String, nullable=True)
    camera_sensitivity_day_x10000 = Column(Integer, nullable=True)
    camera_operating_temperature_min = Column(Integer, nullable=True)
    camera_operating_temperature_max = Column(Integer, nullable=True)
    camera_resolution = Column(Integer, nullable=True)
    camera_power_supply_poe = Column(Boolean, nullable=True)
