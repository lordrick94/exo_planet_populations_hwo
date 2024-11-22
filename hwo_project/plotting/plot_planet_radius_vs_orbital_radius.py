import pandas as pd
import matplotlib.pyplot as plt

from hwo_project.data import data_utils

# Load the updated planets data
df = data_utils.load_data('planet_catalog')

# Define colors for each planet type
colors = {
    'mercuries': 'red',
    'venuses': 'orange',
    'earths': 'green',
    'frozen_planets': 'blue',
    'neptunes': 'purple',
    'hot_jupiters': 'brown',
    'gas_giants': 'pink',
}

# Define markers for each planet type
markers = {
    'mercuries': 'D',
    'venuses': 's',
    'earths': 'o',
    'frozen_planets': '^',
    'neptunes': 'v',
    'hot_jupiters': '>',
    'gas_giants': '<',
}

# Plot the contrast vs angular separation
plt.figure(figsize=(10, 8))
for planet_type, group in df.groupby('planet_type'):
    plt.scatter(
        group['eff_orbital_radius'],
        group['planet_radius'],
        color=colors[planet_type],
        marker=markers[planet_type],
        label=planet_type,
    )

plt.xlabel('Orbital Radius (AU)')
plt.ylabel('Planet Radius (Earth Radii)')

plt.xscale('log')
plt.yscale('log')
plt.title('Planet Radius vs Orbital Radius')
plt.legend()                                     

# Show the plot
plt.show()
