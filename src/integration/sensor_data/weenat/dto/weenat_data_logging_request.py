from dataclasses import dataclass
from typing import List


@dataclass
class WeenatDataLoggingRequest:
    """
    This class represents a data logging request for the Weenat service.

    Attributes:
        measurements (List[str]): A list of measurement names.

    Methods:
        as_json(): Returns the data logging request as a JSON string.

    """
    measurements: List[str]

    def as_json(self):
        """
        Returns the data logging request as a JSON string.

        Returns:
            str: The data logging request as a JSON string.

        """
        return "{\"measurements\": [" + ",".join(self.measurements) + "]}"
