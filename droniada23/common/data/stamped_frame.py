from typing import NamedTuple
import numpy as np

from .telemetry import Telemetry


class StampedFrame(NamedTuple):
    frame: np.ndarray
    timestamp: float
    telemetry: Telemetry
