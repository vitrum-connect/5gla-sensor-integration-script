from dataclasses import dataclass
from typing import List

from src.integration.sensor_data.agvolution.dto.timeseries_value import TimeseriesValue


@dataclass
class TimeseriesEntry:
    """
    A class representing a single entry in a timeseries.

    Attributes:
        key (str): The key of the timeseries entry.
        unit (str): The unit of measurement for the timeseries values.
        aggregate (str): The type of aggregation for the timeseries values.
        values (List[TimeseriesValue]): The list of timeseries values.

    """
    key: str
    unit: str
    aggregate: str
    values: List[TimeseriesValue]

    def as_json(self):
        """
        Returns the timeseries entry as a JSON string.

        Returns:
            str: The timeseries entry as a JSON string.

        """
        return "{\"key\": \"" + self.key + "\", \"unit\": \"" + self.unit + "\", \"aggregate\": \"" + self.aggregate + "\", \"values\": [" + ",".join(
            [value.as_json() for value in self.values]) + "]}"
