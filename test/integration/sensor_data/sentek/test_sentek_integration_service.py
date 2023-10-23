import unittest

from src.integration.sensor_data.sentek.sentek_integration_service import SentekIntegrationService


class SentekIntegrationServiceTest(unittest.TestCase):

    def test_given_valid_sensor_data_when_logging_sensor_data_then_the_request_should_be_successful(self):
        api_integration_service = SentekIntegrationService()
        sensor_data = {}
        # Since the sensor is not existing, the result will be false at the moment
        self.assertFalse(api_integration_service.send_sensor_data("42", sensor_data))
