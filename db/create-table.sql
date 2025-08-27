-- создать таблицу cameras
CREATE TABLE `cameras`
(   
    `camera_id` Int64 NOT NULL,
    `camera_model` Utf8 NOT NULL,
    `camera_sensitivity_raw` Utf8 NULL,
    `camera_operating_temperature_raw` Utf8 NULL,
    `camera_data_transfer_interface` Utf8 NULL,
    `camera_case_type` Utf8 NULL,
    `camera_resolution_raw` Utf8 NULL,
    `camera_lens_type` Utf8 NULL,
    `camera_IR_illumination` Int64 NULL,
    `camera_compression_codec` Utf8 NULL,
    `camera_memory_card_support` Utf8 NULL,
    `camera_audio_inputs_outputs` Utf8 NULL,
    `camera_alarm_inputs_outputs` Utf8 NULL,
    `camera_SATA_quantity_capacity` Utf8 NULL,
    `camera_independent_video_outputs` Utf8 NULL,
    `camera_data_transfer_rate` Utf8 NULL,
    `camera_lightning_protection` Bool NULL,
    `camera_power_raw` Utf8 NULL,
    `camera_power_supply_raw` Utf8 NULL,
    `camera_comment` Utf8 NULL,
    `camera_sensitivity_day_x10000` Int64 NULL,
    `camera_operating_temperature_min` Int64 NULL,
    `camera_operating_temperature_max` Int64 NULL,
    `camera_resolution` Int64 NULL,
    `camera_power_x10` Int64 NULL,
    `camera_power_supply_poe` Bool NULL,
    PRIMARY KEY (`camera_id`)
);
--

-- создать таблицу users
CREATE TABLE `users`
(
    `user_id` Int64 NOT NULL,

    `camera_resolution` Int64 NOT NULL,
    `camera_sensitivity_day_x10000` Int64 NOT NULL,
    `camera_IR_illumination` Int64 NOT NULL,
    `camera_operating_temperature_min` Int64 NOT NULL,
    `camera_operating_temperature_max` Int64 NOT NULL,
    `camera_data_transfer_interface` Utf8 NOT NULL,
    `camera_power_supply_poe` Bool NOT NULL,
    `camera_lightning_protection` Bool NOT NULL,
    `camera_comment` Utf8 NOT NULL,

    `search_camera_resolution` Bool NOT NULL,
    `search_camera_sensitivity_day_x10000` Bool NOT NULL,
    `search_camera_IR_illumination` Bool NOT NULL,
    `search_camera_operating_temperature_min` Bool NOT NULL,
    `search_camera_operating_temperature_max` Bool NOT NULL,
    `search_camera_data_transfer_interface` Bool NOT NULL,
    `search_camera_power_supply_poe` Bool NOT NULL,
    `search_camera_lightning_protection` Bool NOT NULL,
    `search_camera_comment` Bool NOT NULL,
    PRIMARY KEY (`user_id`)
);
