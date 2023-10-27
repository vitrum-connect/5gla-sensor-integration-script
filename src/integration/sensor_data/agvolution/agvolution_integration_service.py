import logging

from src.config.config_manager import ConfigManager
from src.integration.sensor_data.agvolution.dto.agvolution_data_logging_request import \
    AgvolutionDataLoggingRequest
from src.integration.sensor_data.agvolution.dto.series_entry import SeriesEntry
from src.integration.sensor_data.agvolution.dto.timeseries_entry import TimeseriesEntry
from src.integration.sensor_data.agvolution.dto.timeseries_value import TimeseriesValue
from src.integration.sensor_data.common_sensor_integration_service import CommonSensorDataIntegrationService


class AgvolutionIntegrationService:

    def __init__(self):
        self._config_manager = ConfigManager()
        self._common_sensor_integration_service = CommonSensorDataIntegrationService()

    def send_sensor_data(self, sensor_id, sensor_data):
        """
        Send sensor data to Agvolution integration service.

        :param sensor_id: The ID of the sensor sending the data.
        :type sensor_id: str
        :param sensor_data: The data to be sent by the sensor.
        :type sensor_data: dict
        :return: None
        """
        return self._common_sensor_integration_service.send_sensor_data(self._url(sensor_id),
                                                                        self._transform_sensor_data_to_request_body(
                                                                            sensor_data))

    def _url(self, sensor_id):
        """
        Constructs the URL for data logging in Agvolution based on the given sensor ID.

        Parameters:
        - sensor_id (str): The ID of the sensor for which the data logging URL is being constructed.

        Returns:
        - url (str): The constructed URL for data logging in Agvolution.

        """
        return self._config_manager.get('api_url') + self._config_manager.get(
            'api_agvolution_data_logging_endpoint') + "/" + sensor_id

    def _transform_sensor_data_to_request_body(self, sensor_data):
        """
        Transforms sensor data into request body for Agvolution data logging.

        Parameters:
        - sensor_data (dict): The sensor data to be transformed.

        Returns:
        - request_data (dict): The transformed request body for Agvolution data logging.

        Example Usage:
        sensor_data = {
            'sensor_id': '12345',
            'timestamp': '2021-10-01T10:00:00',
            'values': [
                {'name': 'temperature', 'value': 25.0},
                {'name': 'humidity', 'value': 50.0}
            ]
        }

        agvolution_service = AgvolutionIntegrationService()
        request_data = agvolution_service._transform_sensor_data_to_request_body(sensor_data)
        """
        series_entry = self._transform_sensor_data_to_series_entry(sensor_data)
        request_data = AgvolutionDataLoggingRequest(series_entry).as_json()
        logging.debug(request_data)
        return request_data

    @staticmethod
    def _transform_sensor_data_to_series_entry(sensor_data):
        # FIXME Dummy implementation, should be done on the real data.
        series_entry = SeriesEntry(
            device="42",
            longitude=8.170879,
            latitude=52.503075,
            timeseries=[
                TimeseriesEntry(
                    key="some_key",
                    unit="some_unit",
                    aggregate="",
                    values=[
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=2.0
                        ),
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=4.0
                        ),
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=8.0
                        ),
                    ]
                ),
                TimeseriesEntry(
                    key="some_other_key",
                    unit="some_other_unit",
                    aggregate="",
                    values=[
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=2.0
                        ),
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=4.0
                        ),
                        TimeseriesValue(
                            time="2023-03-17T06:41:35.834",
                            value=8.0
                        ),
                    ]
                )
            ]
        )
        return series_entry
