import numpy as np
import matplotlib.pyplot as plt

# Define the function from utils.py
def get_optimal_obs_pos(inclination):
    """
    Get the optimal observation position for a given inclination.

    :param inclination: Inclination of the star orbits (in degrees).
    :return: The optimal observation position (in degrees).
    """
    return np.degrees(np.arcsin(1 / (2 * np.sin(np.radians(inclination)))))

# Generate data points for inclination from 0 to 90 degrees
inclinations = np.linspace(0.001, 90, 1000)  # Avoid 0 to prevent division by zero

# Compute the optimal observation positions for each inclination
optimal_positions = [get_optimal_obs_pos(inc) for inc in inclinations]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(inclinations, optimal_positions, label='Optimal Observation Position')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Optimal Observation Position (degrees)')
plt.title('Inclination vs Optimal Observation Position')
plt.legend()
plt.grid(True)
plt.show()