import logging
import time

import requests

from src.config.config_manager import ConfigManager


class CommonSensorDataIntegrationService:
    """
    Sends sensor data to a specified URL with built-in retry mechanism.

    :param url: The URL to which the sensor data will be sent.
    :param transformed_sensor_data: The transformed sensor data that will be sent.
    :return: True if the sensor data is sent successfully, False otherwise.
    """

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
        headers = {'X-API-Key': config_manager.get_env('API_KEY'), 'Content-Type': 'application/json'}
        response = requests.post(url=url, headers=headers, data=transformed_sensor_data)
        if response.status_code == 201:
            return True
        else:
            logging.error(f"API is not available. Status code: {response.status_code}")
            logging.error(f"The response from the service was: {response.text}")
            return False
