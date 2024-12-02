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

# Define sizes for each planet type
sizes = {
    'mercuries': 50,
    'venuses': 70,
    'earths': 90,
    'frozen_planets': 110,
    'neptunes': 130,
    'hot_jupiters': 150,
    'gas_giants': 170,
}

# Create a figure with three rows and two columns
plt.figure(figsize=(25, 15))

# Plot 1: orbital radius < 1.5 and planet_radius < 1.5
plt.subplot(3, 2, 5)
filtered_df = df[(df['orbital_radius'] < 1.5) & (df['planet_radius'] < 1.5)]
for planet_type, group in filtered_df.groupby('planet_type'):
    plt.scatter(
        group['orbital_radius'],
        group['planet_radius'],
        color=colors[planet_type],
        s=sizes[planet_type],
        label=planet_type,
        alpha=0.7
    )
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(r'', fontsize=20)
plt.ylabel('', fontsize=20)
plt.title('', fontsize=20)
plt.xscale('log')
plt.legend(fontsize=20)


# Plot 2: planet radius > 1.5 and planet_radius < 6
plt.subplot(3, 1, 2)
filtered_df = df[(df['planet_radius'] > 1.5) & (df['planet_radius'] < 6)]
for planet_type, group in filtered_df.groupby('planet_type'):
    plt.scatter(
        group['orbital_radius'],
        group['planet_radius'],
        color=colors[planet_type],
        s=sizes[planet_type],
        label=planet_type,
        alpha=0.7
    )
plt.xlabel(r'Orbital Radius (AU)', fontsize=20)
plt.ylabel('Planet Radius (Earth Radii)', fontsize=20)
plt.title('', fontsize=20)
plt.xscale('log')
plt.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


# Plot 3: orbital radius > 1.5 and planet_radius < 6
plt.subplot(3,2,6)
filtered_df = df[(df['orbital_radius'] > 1.5) & (df['planet_radius'] < 6)]
for planet_type, group in filtered_df.groupby('planet_type'):
    plt.scatter(
        group['orbital_radius'],
        group['planet_radius'],
        color=colors[planet_type],
        s=sizes[planet_type],
        label=planet_type,
        alpha=0.7
    )
plt.xlabel(r'', fontsize=20)
plt.ylabel('', fontsize=20)
plt.title('', fontsize=20)
plt.xscale('log')
plt.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# Plot 4: planet_radius > 6
plt.subplot(3, 1, 1)
filtered_df = df[df['planet_radius'] > 6]
for planet_type, group in filtered_df.groupby('planet_type'):
    plt.scatter(
        group['orbital_radius'],
        group['planet_radius'],
        color=colors[planet_type],
        s=sizes[planet_type],
        label=planet_type,
        alpha=0.7
    )
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(r'', fontsize=20)
plt.ylabel('', fontsize=20)
plt.title('Simulated Planet Populations', fontsize=20)
plt.xscale('log')
plt.legend(fontsize=20)


# Adjust layout
plt.tight_layout(rect=[0.02, 0., 1, 1])

# Save and show the plot
plt.savefig(data_utils.get_fig_dir_path()+'simulated_planet_populations.png', dpi=800)

#plt.show()