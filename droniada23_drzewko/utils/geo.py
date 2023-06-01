import numpy as np
from geographiclib.geodesic import Geodesic


GEOD = Geodesic.WGS84


def solve_inverse(lat0: float, lon0: float, lat1: float, lon1: float) -> tuple[float, float]:
    res = GEOD.Inverse(lat0, lon0, lat1, lon1)
    dist = res['s12']
    angle = np.deg2rad(-res['azi1'] + 90)
    x = dist * np.cos(angle)
    y = dist * np.sin(angle)
    return x, y


def solve_direct(lat0: float, lon0: float, dx: float, dy: float) -> tuple[float, float]:
    azi = np.rad2deg(np.arctan2(dx, dy))
    dist = np.linalg.norm((dx, dy))
    res = GEOD.Direct(lat0, lon0, azi, dist)
    return res['lat2'], res['lon2']
