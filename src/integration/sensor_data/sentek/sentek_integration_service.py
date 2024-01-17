import json
import logging
from dataclasses import asdict

from src.config.config_manager import ConfigManager
from src.integration.sensor_data.common_sensor_integration_service import CommonSensorDataIntegrationService
from src.integration.sensor_data.sentek.dto.reading import Reading
from src.integration.sensor_data.sentek.dto.sentek_data_logging_request import SentekDataLoggingRequest


class SentekIntegrationService:

    def __init__(self):
        self._config_manager = ConfigManager()
        self._common_sensor_integration_service = CommonSensorDataIntegrationService()

    def send_sensor_data(self, sensor_id, sensor_data):
        """

        Send Sensor Data

        Sends the sensor data to the integration service.

        Parameters:
        - sensor_id (str): The ID of the sensor.
        - sensor_data (dict): The sensor data to be sent.

        Returns:
        None

        """
        return self._common_sensor_integration_service.send_sensor_data(self._url(sensor_id),
                                                                        self._transform_sensor_data_to_request_body(
                                                                            sensor_data))

    def _url(self, sensor_id):
        """

          This method `_url` is a private method of the `SentekIntegrationService` class.

          Parameters:
            - sensor_id: A string value representing the ID of the sensor.

          Returns:
            - A string value representing the URL for the Sentek data logging endpoint.

          Description:
            - This method constructs the URL for the Sentek data logging endpoint based on the given sensor ID. It uses the configuration manager to fetch the API URL and the endpoint from the application's configuration.
            - The constructed URL is returned as a string.
            - This method is intended to be used internally within the `SentekIntegrationService` class and should not be called directly.

          Example usage:
            config_manager = ConfigManager()
            service = SentekIntegrationService(config_manager)

            sensor_id = "ABC123"
            url = service._url(sensor_id)
            print(url)

            Output:
            https://api.example.com/sentek-data-logging/ABC123

        """
        return self._config_manager.get_env('API_URL') + self._config_manager.get(
            'api_sentek_data_logging_endpoint') + "/" + sensor_id

    def _transform_sensor_data_to_request_body(self, sensor_data):
        """
        Transforms the sensor data into the request body format for Sentek data logging.

        :param sensor_data: The sensor data to be transformed.
        :return: The transformed sensor data in request body format.

        """
        readings = self._transform_sensor_data_to_readings(sensor_data)
        readings_as_json = self._transform_readings_to_json(readings)
        request_data = SentekDataLoggingRequest(readings_as_json).as_json()
        logging.debug(request_data)
        return request_data

    @staticmethod
    def _transform_readings_to_json(readings):
        """
        Transforms a list of readings into a list of JSON strings.

        Args:
            readings (list): A list of reading objects.

        Returns:
            list: A list of JSON strings representing the readings.

        """
        readings_as_json = []
        for reading in readings:
            readings_as_json.append(json.dumps(asdict(reading)))
        return readings_as_json

    @staticmethod
    def _transform_sensor_data_to_readings(sensor_data):
        # FIXME Dummy implementation, should be done on the real data.
        first_reading = Reading(
            '2023-03-17T06:41:35.834',
            2.0,
            4.0,
            8.0,
            16.0,
            32.0,
            64.0,
            128.0,
            256.0,
            512.0,
            1024.0,
            2048.0,
            4096.0,
            8192.0,
            16384.0,
            32768.0,
            65536,
            131072,
            262144,
            524288,
            1048576
        )
        second_reading = Reading(
            '2023-06-19T06:42:14.844',
            2.0,
            4.0,
            8.0,
            16.0,
            32.0,
            64.0,
            128.0,
            256.0,
            512.0,
            1024.0,
            2048.0,
            4096.0,
            8192.0,
            16384.0,
            32768.0,
            65536,
            131072,
            262144,
            524288,
            1048576
        )
        return [first_reading, second_reading]
