from typing import NamedTuple


class Telemetry(NamedTuple):
    lat: float
    lon: float
    alt: float
    hdg: float

    def to_csv_line(self, timestamp: float) -> str:
        return f'{timestamp},{self.lat},{self.lon},{self.alt},{self.hdg}\n'
