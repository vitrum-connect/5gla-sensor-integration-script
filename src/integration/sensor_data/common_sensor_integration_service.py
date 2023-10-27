import logging
import time

import requests

from src.config.config_manager import ConfigManager
from src.integration.sensor_data.dto.request.register_device_request import RegisterDeviceRequest


class CommonSensorDataIntegrationService:
    """
    Sends sensor data to a specified URL with built-in retry mechanism.

    :param url: The URL to which the sensor data will be sent.
    :param transformed_sensor_data: The transformed sensor data that will be sent.
    :return: True if the sensor data is sent successfully, False otherwise.
    """

    def register_device(self, manufacturer, sensor_id, latitude, longitude):
        """
        Registers a device with the given information.

        Args:
            manufacturer (str): The manufacturer of the device.
            sensor_id (str): The unique identifier of the device.
            latitude (float): The latitude of the device location.
            longitude (float): The longitude of the device location.

        Returns:
            bool: True if the device was successfully registered, False otherwise.

        Note:
            This method sends a POST request to the device registration endpoint using the configured API key
            and the provided device information. The request is JSON formatted.
            If the response status code is 201, indicating a successful registration, the method returns True.
            If the response status code is not 201, indicating an unsuccessful registration, the method returns False
            and logs an error message with the response status code and text.
        """
        config_manager = ConfigManager()
        headers = {
            'X-API-Key': config_manager.get_env('API_KEY'),
            'Content-Type': 'application/json'
        }
        url = config_manager.get('api_url') + config_manager.get('device_registration_endpoint')
        response = requests.post(url=url, headers=headers,
                                 data=RegisterDeviceRequest(manufacturer=manufacturer, id=sensor_id, latitude=latitude,
                                                            longitude=longitude).as_json())
        if response.status_code == 201:
            return True
        else:
            logging.error(f"Request was not successful. Status code: {response.status_code}")
            logging.error(f"The response from the service was: {response.text}")
            return False

    def send_sensor_data(self, url, transformed_sensor_data):
        """

        Sends sensor data to a specified URL with built-in retry mechanism.

        Parameters:
        - url (str): The URL to which the sensor data will be sent.
        - transformed_sensor_data (dict): The transformed sensor data that will be sent.

        Returns:
        - True if the sensor data is sent successfully, False otherwise.

        """
        max_retries = ConfigManager().get('max_retries')
        for i in range(max_retries):
            if self._send_sensor_data(url, transformed_sensor_data):
                return True
            else:
                logging.info(f"Retrying to send sensor_data. Attempt {i + 1}/{max_retries}")
                retry_delay_seconds = ConfigManager().get('retry_delay_seconds')
                logging.info(f"Sleeping for {retry_delay_seconds} seconds.")
                time.sleep(retry_delay_seconds)
        logging.error(f"Failed to send sensor data after {max_retries} attempts.")
        return False

    @staticmethod
    def _send_sensor_data(url, transformed_sensor_data):
        """
        Send sensor data to the given URL.

        Parameters:
        - url (str): The URL to send the sensor data to.
        - transformed_sensor_data (dict): The transformed sensor data to send.

        Returns:
        - bool: True if the sensor data was sent successfully, False otherwise.
        """
        config_manager = ConfigManager()
        headers = {
            'X-API-Key': config_manager.get_env('API_KEY'),
            'Content-Type': 'application/json'
        }
        response = requests.post(url=url, headers=headers, data=transformed_sensor_data)
        if response.status_code == 201:
            return True
        else:
            logging.error(f"Request was not successful. Status code: {response.status_code}")
            logging.error(f"The response from the service was: {response.text}")
            return False
