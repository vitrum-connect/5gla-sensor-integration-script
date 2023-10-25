from dataclasses import dataclass


@dataclass
class TimeseriesValue:
    """
    TimeseriesValue class represents a single data point in a time series.

    Attributes:
        time (str): The timestamp of the data point in ISO 8601 format.
        value (float): The value of the data point.

    """
    time: str
    value: float

    def as_json(self):
        """
        Returns the timeseries value as a JSON string.

        Returns:
            str: The timeseries value as a JSON string.

        """
        return "{\"time\": \"" + self.time + "\", \"value\": " + str(self.value) + "}"
