from dataclasses import dataclass
from typing import List

from src.integration.sensor_data.agvolution.dto.timeseries_entry import TimeseriesEntry


@dataclass
class SeriesEntry:
    """
    Class representing a series entry.

    Attributes:
        device (str): The device associated with the series entry.
        longitude (float): The longitude of the location associated with the series entry.
        latitude (float): The latitude of the location associated with the series entry.
        timeseries (List[TimeseriesEntry]): The list of timeseries entries associated with the series entry.
    """
    device: str
    longitude: float
    latitude: float
    timeseries: List[TimeseriesEntry]

    def as_json(self):
        """
        Returns the series entry as a JSON string.

        Returns:
            str: The series entry as a JSON string.

        """
        return "{\"device\": \"" + self.device + "\", \"longitude\": " + str(
            self.longitude) + ", \"latitude\": " + str(
            self.latitude) + ", \"timeseries\": [" + ",".join(
            [timeseries_entry.as_json() for timeseries_entry in self.timeseries]) + "]}"
