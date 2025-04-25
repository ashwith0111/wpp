import numpy as np
def cartesian_to_polar(cartesian_points):
    x = cartesian_points[:, 0]
    y = cartesian_points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    polar_points = np.vstack((r, theta)).T
    return polar_points
N = 10
cartesian_points = np.random.uniform(-10, 10, size=(N, 2))
polar_points = cartesian_to_polar(cartesian_points)
print("Cartesian Coordinates (x, y):")
print(cartesian_points)
print("\nPolar Coordinates (r, theta):")
print(polar_points)