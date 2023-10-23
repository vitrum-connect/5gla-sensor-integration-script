from dataclasses import dataclass
from typing import List


@dataclass
class SentekDataLoggingRequest:
    """

    Class: SentekDataLoggingRequest

        Represents a data logging request for Sentek sensors.

    Attributes:

        readings (List[str]): A list of sensor readings to be logged.

    """
    readings: List[str]

    def as_json(self):
        """
        Returns the data logging request as a JSON string.

        Returns:
            str: The data logging request as a JSON string.

        """
        return "{\"readings\": [" + ",".join(self.readings) + "]}"
