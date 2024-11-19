import pandas as pd
import matplotlib.pyplot as plt

# Load the updated planets data
df = pd.read_csv('updated_planets.csv')

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

for planet_type in colors.keys():
    mask = df['planet_type'] == planet_type
    plt.scatter(df[mask]['angular_separation'], df[mask]['contrast'], 
                c=colors[planet_type], marker=markers[planet_type], 
                label=planet_type, alpha=0.6, edgecolor='black')

plt.xlabel('Angular Separation (arcsec)', fontsize=14)
plt.xlim(0, 0.3)
plt.ylabel('Contrast', fontsize=14)
plt.yscale('log')
plt.title('Contrast vs Angular Separation', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('contrast_vs_angular_separation.png')
plt.show()