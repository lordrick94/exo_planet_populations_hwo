import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from hwo_project.data import data_utils
from IPython import embed

def load_probability_grid(file_path):
    return np.load(file_path)

def simulate_random_planets(R, P, grid, nplanets=30000, seed=None):
    if seed is not None:
        np.random.seed(seed)

    r_A_pdf = grid.flatten()
    cum_sum = np.cumsum(r_A_pdf)
    cum_sum /= cum_sum[-1]

    randu = np.random.uniform(size=nplanets)
    uidx = [np.argmin(np.abs(irand - cum_sum)) for irand in tqdm(randu, total=nplanets, desc='Generating Random Planets')]
    idx = np.unravel_index(uidx, grid.shape)

    planet_rad = R[idx[0]]
    period_days = P[idx[1]]

    return pd.DataFrame({'planet_radius': planet_rad, 'Period(Days)': period_days})

def save_planets_to_csv(planets_df):
    file_path = data_utils.load_data('random_planets', get_path=True)
    planets_df.to_csv(file_path, index=False)

def plot_scatter(planets_df):
    # Set the style
    sns.set(style="whitegrid")

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(14, 10))

    # Plot the scatter plot
    sc = ax.scatter(
        planets_df['Period(Days)'], 
        planets_df['planet_radius'], 
        c=planets_df['planet_radius'], 
        cmap='plasma', 
        s=100, 
        alpha=0.8, 
        edgecolors='k', 
        linewidth=0.6
    )

    # Add color bar
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Planet Radius (R)', fontsize=24)

    # Calculate mean and median
    mean_period = planets_df['Period(Days)'].mean()
    median_period = planets_df['Period(Days)'].median()
    mean_radius = planets_df['planet_radius'].mean()
    median_radius = planets_df['planet_radius'].median()

    # # Add vertical and horizontal lines for mean and median
    # ax.axvline(mean_period, color='blue', linestyle='--', linewidth=2, label=f'Mean Period: {mean_period:.2f} days')
    # ax.axvline(median_period, color='green', linestyle='-', linewidth=2, label=f'Median Period: {median_period:.2f} days')
    # ax.axhline(mean_radius, color='red', linestyle='--', linewidth=2, label=f'Mean Radius: {mean_radius:.2f} R')
    # ax.axhline(median_radius, color='orange', linestyle='-', linewidth=2, label=f'Median Radius: {median_radius:.2f} R')

    # Customize the plot
    ax.set_xlabel('Period (Days) (P)', fontsize=24, labelpad=15)
    ax.set_ylabel('Planet Radius (R)', fontsize=24, labelpad=15)
    ax.set_title('Randomly Generated Planets', fontsize=24, pad=20)
    ax.legend(fontsize=18)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add a background color to the plot area
    ax.set_facecolor('whitesmoke')

    # Adjust layout
    plt.tight_layout()

    # Save the figure with high resolution
    fig_dir = data_utils.get_fig_dir_path()
    plt.savefig(fig_dir + 'random_planets_scatter_presentation.png', dpi=800)

    # Show the plot
    plt.show()

def plot_histograms(planets_df):
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Histogram for planet radius
    axs[0].hist(np.log10(planets_df['planet_radius']), bins=20, alpha=0.7, edgecolor='black', color='skyblue')
    axs[0].set_xlabel('log(Planet Radius)', fontsize=16, labelpad=15)
    axs[0].set_ylabel('N', fontsize=16, labelpad=15)
    axs[0].set_title('Distribution of Planet Radius', fontsize=20, pad=20)
    axs[0].grid(True, linestyle='--', alpha=0.7)
    axs[0].set_facecolor('whitesmoke')

    # Histogram for period
    axs[1].hist(np.log10(planets_df['Period(Days)']), bins=20, alpha=0.7, edgecolor='black', color='lightgreen')
    axs[1].set_xlabel('log(Period(Days))', fontsize=16, labelpad=15)
    axs[1].set_ylabel('N', fontsize=16, labelpad=15)
    axs[1].set_title('Distribution of Period (Days)', fontsize=20, pad=20)
    axs[1].grid(True, linestyle='--', alpha=0.7)
    axs[1].set_facecolor('whitesmoke')

    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.4)

    # Adjust layout to fit labels
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save the figure with high resolution
    fig_dir = data_utils.get_fig_dir_path()
    plt.savefig(fig_dir + 'random_planets_histograms_presentation.png', dpi=800)

    # Show the plot
    plt.show()

def gen_random_planets(nplanets=25000, show_plots=True, seed=None):
    grid = data_utils.load_data('pdf_grid')
    R = np.arange(0.67, 17.1, 0.1)
    P = np.arange(10, 640, 1)
    random_planets = simulate_random_planets(R=R, P=P, nplanets=nplanets, grid=grid, seed=seed)
    save_planets_to_csv(random_planets)
    if show_plots:
        plot_scatter(random_planets)
        plot_histograms(random_planets)

if __name__ == "__main__":
    gen_random_planets(30000)