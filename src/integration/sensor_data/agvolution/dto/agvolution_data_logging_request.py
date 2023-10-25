from dataclasses import dataclass

from src.integration.sensor_data.agvolution.dto.series_entry import SeriesEntry


@dataclass
class AgvolutionDataLoggingRequest:
    series_entry: SeriesEntry

    def as_json(self):
        """
        Returns the data logging request as a JSON string.

        Returns:
            str: The data logging request as a JSON string.

        """
        return "{\"seriesEntry\": " + self.series_entry.as_json() + "}"
