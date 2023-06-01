from typing import NamedTuple
import numpy as np

from droniada23_drzewko.data.telemetry import Telemetry


class StampedFrame(NamedTuple):
    frame: np.ndarray
    timestamp: float
    telemetry: Telemetry
