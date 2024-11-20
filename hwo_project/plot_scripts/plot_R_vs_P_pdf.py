import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def plot_grid(R, P, integral_values):
    """
    Function to plot a grid of P and R values with the corresponding integral values.

    Parameters:
    P, R : Arrays of P and R values.
    integral_values : Array of integral values corresponding to each (P, R) pair.
    """
    plt.figure(figsize=(10, 8))
    ax = plt.gca()

    # Apply a logarithmic color scale for the occurrence rate
    norm = colors.LogNorm(vmin=0.001, vmax=100)

    # Calculate the extent to ensure grid matches bin edges
    extent = [P[0] - (P[1] - P[0]) / 2, P[-1] + (P[-1] - P[-2]) / 2,
              R[0] - (R[1] - R[0]) / 2, R[-1] + (R[-1] - R[-2]) / 2]

    # Use imshow to plot a grid with equally sized cells
    im = ax.imshow(integral_values, cmap='plasma', norm=norm, aspect='auto',
                   extent=extent, origin='lower')

    # Add a colorbar to show the scale of occurrence rates
    cbar = plt.colorbar(im, label='Occurrence Rate [%]')
    cbar.ax.yaxis.label.set_size(12)

    plt.xlabel('Orbital Period [days]', fontsize=12)
    plt.ylabel('Planet Radius [R⊕]', fontsize=12)
    plt.title('G Star Occurrence Rate [%] From Toymodel', fontsize=14, color='w')

    # Calculate midpoints of bins for tick labels
    P_centers = 0.5 * (P[:-1] + P[1:])
    R_centers = 0.5 * (R[:-1] + R[1:])

    # Set ticks to be in the middle of each bin
    ax.set_xticks(P)
    ax.set_yticks(R)

    # Set tick labels
    ax.set_xticklabels([f'{p:.0f}' for p in P])
    ax.set_yticklabels([f'{r:.2f}' for r in R])

    # Add integral values (occurrence rates) to the center of each grid cell
    for i in range(integral_values.shape[0]):
        for j in range(integral_values.shape[1]):
            plt.text(P_centers[j], R_centers[i], f'{integral_values[i, j]:.2f}%', 
                     ha='center', va='center', color='black', fontsize=8, weight='bold')

    # Set background to black for contrast (as in the uploaded image)
    ax.set_facecolor('black')
    plt.show()

# Example usage
R = np.array([0.67, 1.72, 3.88, 5.16, 7.6, 17])
P = np.array([10, 20, 40, 80, 160, 320, 640])
integral_values = np.array([[0.001, 0.02, 0.04, 0.07, 0.11, 0.17],
                            [0.335, 0.527, 0.73, 0.92, 1.12, 2.72],
                            [0.85, 1.28, 1.94, 2.92, 3.6, 5.0],
                            [1.35, 2.14, 3.89, 5.93, 7.75, 9.29],
                            [3.55, 5.85, 7.96, 9.74, 12.08, 13.88]])

plot_grid(R, P, integral_values)
