from dataclasses import dataclass

from src.integration.sensor_data.weenat.dto.measurement_values import MeasurementValues


@dataclass
class Measurement:
    """
    Class representing a measurement with a timestamp and measurement values.

    Attributes:
        timestamp (str): The timestamp of the measurement.
        measurementValues (MeasurementValues): The measurement values.

    """
    timestamp: str
    measurementValues: MeasurementValues
