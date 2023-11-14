import unittest

from src.api.manufacturer import Manufacturer
from src.integration.sensor_data.common_sensor_integration_service import CommonSensorDataIntegrationService
from src.integration.sensor_data.sentek.sentek_integration_service import SentekIntegrationService


class SentekIntegrationServiceTest(unittest.TestCase):
    sensor_id = "42"

    def test_given_valid_sensor_data_when_logging_sensor_data_then_the_request_should_be_successful(self):
        # Register the device first
        common_sensor_data_integration_service = CommonSensorDataIntegrationService()
        self.assertTrue(
            common_sensor_data_integration_service.register_device(Manufacturer.SENTEK, self.sensor_id, 52.521400,
                                                                   8.197360))

        # Send sensor data
        api_integration_service = SentekIntegrationService()
        sensor_data = {}
        self.assertTrue(api_integration_service.send_sensor_data(self.sensor_id, sensor_data))
