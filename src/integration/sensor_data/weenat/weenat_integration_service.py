import json
import logging
from dataclasses import asdict

from src.config.config_manager import ConfigManager
from src.integration.sensor_data.common_sensor_integration_service import CommonSensorDataIntegrationService
from src.integration.sensor_data.weenat.dto.measurement import Measurement
from src.integration.sensor_data.weenat.dto.measurement_values import MeasurementValues
from src.integration.sensor_data.weenat.dto.weenat_data_logging_request import WeenatDataLoggingRequest


class WeenatIntegrationService:

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
        self._common_sensor_integration_service.send_sensor_data(self._url(sensor_id),
                                                                 self._transform_sensor_data_to_request_body(
                                                                     sensor_data))

    def _url(self, sensor_id):
        """
        Returns the URL for the Weenat API to log sensor data for a specific sensor.

        :param sensor_id: The ID of the sensor.
        :type sensor_id: str
        :return: The URL for logging sensor data for the specified sensor.
        :rtype: str
        """
        return self._config_manager.get('api_url') + self._config_manager.get(
            'api_weenat_data_logging_endpoint') + "/" + sensor_id

    def _transform_sensor_data_to_request_body(self, sensor_data):
        """
        Transforms sensor data to request body format.

        Args:
            sensor_data: The sensor data to transform.

        Returns:
            The transformed request body as a JSON string.
        """
        measurements = self._transform_sensor_data_to_measurements(sensor_data)
        measurements_as_json = self._transform_measurements_to_json(measurements)
        request_data = WeenatDataLoggingRequest(measurements_as_json).as_json()
        logging.debug(request_data)
        return request_data

    @staticmethod
    def _transform_measurements_to_json(measurements):
        measurements_as_json = []
        for measurement in measurements:
            measurements_as_json.append(json.dumps(asdict(measurement)))
        return measurements_as_json

    @staticmethod
    def _transform_sensor_data_to_measurements(sensor_data):
        # FIXME Dummy implementation, should be done on the real data.
        first_measurement = Measurement(
            '2023-03-17T06:41:35.834',
            measurementValues=MeasurementValues(
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
                1048576,
                2097152,
                4194304,
                8388608,
                16777216,
                33554432
            )
        )
        second_measurement = Measurement(
            '2023-06-27T06:21:50.834',
            measurementValues=MeasurementValues(
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
                1048576,
                2097152,
                4194304,
                8388608,
                16777216,
                33554432
            )
        )
        return [first_measurement, second_measurement]
