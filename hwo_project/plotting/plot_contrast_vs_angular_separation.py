import pandas as pd
import matplotlib.pyplot as plt

from hwo_project import utils
from hwo_project.data import data_utils
from hwo_project.planet_simulations import catalog_utils

import astropy.units as u

def plot_contrast_vs_angular_separation():
    # Load the updated planets data
    df = data_utils.load_data('planet_catalog')

    # Get the IWA
    iwa_hwo = utils.calculate_iwa()
    iwa_30m_telescope = utils.calculate_iwa(aperture_diameter=30*u.m)

    num_earths_hwo = catalog_utils.get_num_observable_planets(df, exoplanet_type='earths')
    num_earths_30m_telescope = catalog_utils.get_num_observable_planets(df, exoplanet_type='earths', telescope_type='30m')

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

    # Define font dictionary
    font_dict = {
        'family': 'serif',
        'color': 'darkblue',
        'weight': 'bold',
    }

    # Plot the contrast vs angular separation
    plt.figure(figsize=(12, 10))

    for planet_type in colors.keys():
        mask = df['planet_type'] == planet_type
        plt.scatter(df[mask]['angular_separation'], df[mask]['contrast'], 
                    c=colors[planet_type], marker=markers[planet_type], 
                    label=planet_type, alpha=0.6, edgecolor='black')

    plt.xlabel('Angular Separation (arcsec)', fontsize=14, fontdict=font_dict)
    plt.ylabel('Contrast', fontsize=14, fontdict=font_dict)

    plt.xlim(left=0, right=0.25)
    plt.ylim(1e-11, 1e-2)

    # Add contrast floors and IWA lines
    plt.axhline(1e-10, color='red', linestyle='--', linewidth=2, label='HWO IWA & Contrast Floor', alpha=0.9)
    plt.axvline(iwa_hwo[1].value, color='red', linestyle=':', linewidth=2, alpha=0.9)
    plt.axhline(1e-8, color='gold', linestyle='--', linewidth=2, label='30m Telescope IWA & Contrast Floor', alpha=0.9)
    plt.axvline(iwa_30m_telescope[1].value, color='gold', linestyle=':', linewidth=2, alpha=0.9)

    # Add the number of observable planets text on top
    plt.text(0.08, 1e-3, f"Number of observable Exo-Earths \nHWO: {num_earths_hwo} \n30m Ground Telescope: {num_earths_30m_telescope}", fontsize=14, fontdict=font_dict, 
             bbox=dict(facecolor='limegreen', alpha=0.5))

    # Add shaded regions
    plt.fill_betweenx(y=[0, 1e-10], x1=0, x2=5, color='grey', alpha=0.8,label='Unobservable Region')
    plt.fill_betweenx(y=[1e-10, 1e-8], x2=iwa_hwo[1].value, x1=iwa_30m_telescope[1].value, color='grey', alpha=0.8)
    plt.fill_betweenx(y=[1e-8, 1e-1], x2=iwa_hwo[1].value, x1=iwa_30m_telescope[1].value, color='cornflowerblue', alpha=0.3, label='Observable Only by Ground Telescope')
    plt.fill_betweenx(y=[1e-10, 1e-8], x2=1, x1=iwa_hwo[1].value, color='limegreen', alpha=0.3, label='Observable Only by HWO')
    plt.fill_betweenx(y=[1e-10, 1e-1], x1=0, x2=iwa_30m_telescope[1].value, color='grey', alpha=0.8)

    plt.yscale('log')
    plt.title(r'Estimated Contrast vs Angular Separation for $\lambda=7000A^o$', fontsize=16, fontdict=font_dict)
    plt.grid(True, linestyle='--', alpha=0.3)

    plt.legend(framealpha=0.3)
    plt.tight_layout()
    plt.savefig(data_utils.get_fig_dir_path() + 'contrast_vs_angular_separation.png', dpi=800)
    plt.show()

if __name__ == '__main__':
    plot_contrast_vs_angular_separation()