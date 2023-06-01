from . import geo


def geo_project(xp: float, yp: float, lat0: float, lon0: float, alt0: float, f_len_px: float) -> tuple[float, float]:
    xm = alt0 * xp / f_len_px
    ym = -alt0 * yp / f_len_px
    lat, lon = geo.solve_direct(lat0, lon0, xm, ym)
    return lat, lon
