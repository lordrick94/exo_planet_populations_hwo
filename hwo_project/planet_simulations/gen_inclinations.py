import numpy as np
import matplotlib.pyplot as plt 
def generate_mock_i(n_simulated_i, show_plot=False,seed=42):
    """
    Generate a mock sample of i values using the CDF of the observed i values.
    :param original_array: Array of observed i values
    :param n_simulated_i: Number of simulated i values to generate
    :return: Array of simulated i values
    """
    from numpy.random import default_rng

    # Set seed for reproducibility

    rng = default_rng(seed=seed)

    x = rng.uniform(0, 1, n_simulated_i)

    # Generate inclination values (0 to 90 degrees)
    inclinations = np.linspace(0, np.pi / 2, 1000)  # radians

    # PDF: Probability density function as cos(i)
    pdf0 = np.cos(inclinations)

    # Normalize the PDF to create a probability density
    pdf = pdf0/np.trapz(pdf0, inclinations)  # normalization using trapezoidal integration

    # CDF: Cumulative distribution function (integral of PDF)
    cdf = np.cumsum(pdf) * (inclinations[1] - inclinations[0])  # discrete integration
    # Calculate the CDF of the i values
    i_sorted, i_cdf = inclinations, cdf

    # Get the indices 
    idx = np.searchsorted(i_cdf, x, side='left')

    # Check whether the range of i_sorted is OK
    n_zero = np.where(idx==0)[0]
    while len(n_zero) > 0:
        # Regenerate the random values where idx is 0
        x[n_zero] = rng.uniform(0, 1, len(n_zero))
        idx[n_zero] = np.searchsorted(i_cdf, x[n_zero], side='left')
        n_zero = np.where(idx==0)[0]

    # Perform inverse lookup with linear interpolation
    x_pdf = i_sorted[idx-1] + (x-i_cdf[idx-1])/(i_cdf[idx]-i_cdf[idx-1]) * (i_sorted[idx]-i_sorted[idx-1])

    if show_plot:
        # Plot the histogram of the pdf and simulated i values
        plt.figure(figsize=(10, 8))
        
        # Plot the PDF
        plt.plot(np.degrees(inclinations), 400 * pdf0, label='PDF', color='red', linewidth=2)
        
        # Plot the histogram
        plt.hist(np.degrees(x_pdf), bins=50, color='blue', alpha=0.6, label='Simulated i', edgecolor='black')
        
        # Add labels and title
        plt.xlabel('Inclination (degrees)', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.title('Simulated Inclination Distribution', fontsize=16)
        
        # Add grid lines
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Add legend
        plt.legend(fontsize=12)
        
        
        # Show the plot
        plt.show()

    return np.degrees(x_pdf)

if __name__ == '__main__':
    # Generate 1000 simulated i values
    simulated_i = generate_mock_i(13000, show_plot=True)