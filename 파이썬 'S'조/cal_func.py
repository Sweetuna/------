# =========================================================
# 3. 계산 함수
# =========================================================

def get_planet_angle(planet, days):
    angle = np.radians(planet["initial_angle"]) + 2 * np.pi * days / planet["period"]
    return angle % (2 * np.pi)


def get_planet_position(planet, days):
    angle = get_planet_angle(planet, days)
    r = planet["radius"]

    x = r * np.cos(angle)
    y = r * np.sin(angle)

    return x, y


def get_angle_from_position(x, y):
    return np.arctan2(y, x) % (2 * np.pi)


def get_angle_difference(a, b):
    return abs(np.angle(np.exp(1j * (a - b))))