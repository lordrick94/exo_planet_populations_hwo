import pandas as pd
import matplotlib.pyplot as plt

from hwo_project import utils
from hwo_project.data import data_utils
from hwo_project.planet_simulations import catalog_utils

from astropy import units as u

# Load the updated planets data
df = data_utils.load_data('planet_catalog')

# Get the IWA
iwa_hwo = utils.calculate_iwa()

iwa_30m_telescope = utils.calculate_iwa(aperture_diameter=30*u.m)

num_earths = catalog_utils.get_num_observable_planets(df,exoplanet_type='earths')

# Define colors for each planet type
colors = {
    'mercuries': 'magenta',
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
plt.ylabel('Contrast', fontsize=14)

plt.xlim(left=0,right=0.25)
plt.ylim(1e-11,1e-2)
# Add contrast floor
plt.axhline(1e-10, color='red', linestyle='--',linewidth=2, label='HWO IWA & Contrast_floor ',alpha=0.9)

# Add IWA
plt.axvline(iwa_hwo[1].value, color='red', linestyle=':',linewidth=2, label='',alpha=0.9)


# Add contrast floor
plt.axhline(1e-8, color='gold', linestyle='--',linewidth=2, label='30m telescope IWA & Contrast_floor',alpha=0.9)


# Add IWA
plt.axvline(iwa_30m_telescope[1].value, color='gold', linestyle=':',linewidth=2, label='',alpha=0.9)

# Add about the number of observable planets
plt.text(0.05, 1e-10, f"Number of observable Earths: {num_earths}", fontsize=12)



# Add shaded regions
plt.fill_betweenx(y=[0, 1e-10], x1=0, x2=5, color='grey', alpha=0.6)
plt.fill_betweenx(y=[1e-10,1e-8],x2=iwa_hwo[1].value,x1=iwa_30m_telescope[1].value,color='cornflowerblue', alpha=0.6)
plt.fill_betweenx(y=[1e-10,1e-1],x1=0,x2=iwa_30m_telescope[1].value,color='grey', alpha=0.6)

plt.yscale('log')
#plt.xscale('log')
plt.title('Contrast vs Angular Separation', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.3)



plt.legend(framealpha=0.3)
plt.tight_layout()

outfile = data_utils.get_fig_dir_path()
plt.savefig(data_utils.get_fig_dir_path()+'contrast_vs_angular_separation.png',dpi=400)
plt.show()