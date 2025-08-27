from pydantic import BaseModel


class CreateUser(BaseModel):
    # Идентификатор пользователя
    user_id: int

    # Параметры камеры для поиска
    camera_resolution: int = 4
    camera_sensitivity_day_x10000: int = 1000
    camera_IR_illumination: int = 30
    camera_operating_temperature_min: int = -40
    camera_operating_temperature_max: int = 50
    camera_data_transfer_interface: str = "Wi-Fi"
    camera_power_supply_poe: bool = True
    camera_lightning_protection: bool = True
    camera_comment: str = "969"

    # Какие параметры камеры включить в поисковый запрос
    search_camera_resolution: bool = True
    search_camera_sensitivity_day_x10000: bool = True
    search_camera_IR_illumination: bool = True
    search_camera_operating_temperature_min: bool = True
    search_camera_operating_temperature_max: bool = True
    search_camera_data_transfer_interface: bool = False
    search_camera_power_supply_poe: bool = True
    search_camera_lightning_protection: bool = True
    search_camera_comment: bool = False


class DefaultCamera(BaseModel):
    camera_id: int
    camera_model: str

    camera_sensitivity_raw: str = None
    camera_operating_temperature_raw: str = None
    camera_data_transfer_interface: str = None
    camera_case_type: str = None
    camera_resolution_raw: str = None
    camera_lens_type: str = None
    camera_IR_illumination: int = None
    camera_compression_codec: str = None
    camera_memory_card_support: str = None
    camera_audio_inputs_outputs: str = None
    camera_alarm_inputs_outputs: str = None
    camera_SATA_quantity_capacity: str = None
    camera_independent_video_outputs: str = None
    camera_data_transfer_rate: str = None
    camera_lightning_protection: bool = None
    camera_power_raw: str = None
    camera_power_supply_raw: str = None
    camera_comment: str = None
    camera_sensitivity_day_x10000: int = None
    camera_operating_temperature_min: int = None
    camera_operating_temperature_max: int = None
    camera_resolution: int = None
    camera_power_x10: int = None
    camera_power_supply_poe: bool = None
