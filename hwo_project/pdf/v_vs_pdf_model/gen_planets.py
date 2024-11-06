import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_probability_grid(file_path):
    return np.load(file_path)

def generate_random_planets(R, P, nplanets, seed, grid):
    if seed is not None:
        np.random.seed(seed)

    r_A_pdf = grid.flatten()
    cum_sum = np.cumsum(r_A_pdf)
    cum_sum /= cum_sum[-1]

    randu = np.random.uniform(size=nplanets)
    uidx = [np.argmin(np.abs(irand - cum_sum)) for irand in randu]
    idx = np.unravel_index(uidx, grid.shape)

    planet_rad = R[idx[0]]
    period_days = P[idx[1]]

    return pd.DataFrame({'planet_radius': planet_rad, 'Period(Days)': period_days})

def save_planets_to_csv(planets_df, file_path):
    planets_df.to_csv(file_path, index=False)

def plot_scatter(planets_df):
    fig, ax = plt.subplots(figsize=(10, 8))
    sc = ax.scatter(planets_df['Period(Days)'], planets_df['planet_radius'], c=planets_df['planet_radius'], cmap='viridis', s=50, alpha=0.7, edgecolors='w', linewidth=0.5)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Planet Radius (R)')
    ax.set_xlabel('Period(Days) (P)', labelpad=15)
    ax.set_ylabel('Planet Radius (R)', labelpad=15)
    ax.set_title('Randomly Generated Planets')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('random_planets_scatter.png')
    plt.show()

def plot_histograms(planets_df):
    fig, axs = plt.subplots(2, 1, figsize=(10, 12))
    axs[0].hist(np.log10(planets_df['planet_radius']), bins=20, alpha=0.7, edgecolor='black')
    axs[0].set_xlabel('log(Planet Radius)', labelpad=15)
    axs[0].set_ylabel('N', labelpad=15)
    axs[0].set_title('Histogram of log(Planet Radius)')
    axs[0].grid(True, linestyle='--', alpha=0.7)
    axs[1].hist(np.log10(planets_df['Period(Days)']), bins=20, alpha=0.7, edgecolor='black')
    axs[1].set_xlabel('log(Period(Days))', labelpad=15)
    axs[1].set_ylabel('N', labelpad=15)
    axs[1].set_title('Histogram of log(Period(Days))')
    axs[1].grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('random_planets_histograms.png')
    plt.show()

def main():
    grid = load_probability_grid('r_vs_A_pdf_final.npy')
    nplanets = 1000
    seed = 42
    R = np.arange(0.67, 17.1, 0.1)
    P = np.arange(10, 640, 1)
    random_planets = generate_random_planets(R, P, nplanets, seed, grid)
    save_planets_to_csv(random_planets, 'random_planets.csv')
    plot_scatter(random_planets)
    plot_histograms(random_planets)

if __name__ == "__main__":
    main()