from dataclasses import dataclass


@dataclass
class RegisterDeviceRequest:
    """

    The `RegisterDeviceRequest` class is used to represent a request to register a device.

    Attributes:
        manufacturer (str): The manufacturer of the device.
        id (str): The unique identifier of the device.
        latitude (float): The latitude of the device's location.
        longitude (float): The longitude of the device's location.

    """
    manufacturer: str
    id: str
    latitude: float
    longitude: float

    def as_json(self):
        """
        Returns the device registration request as a JSON string.

        Returns:
            str: The device registration request as a JSON string.

        """
        return "{\"manufacturer\": \"" + self.manufacturer + "\", \"id\": \"" + self.id + "\", \"latitude\": " + str(
            self.latitude) + ", \"longitude\": " + str(self.longitude) + "}"
