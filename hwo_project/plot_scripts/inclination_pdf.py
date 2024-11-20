import numpy as np
import matplotlib.pyplot as plt

# Generate inclination values (0 to 90 degrees)
inclinations = np.linspace(0, np.pi / 2, 1000)  # radians

# PDF: Probability density function as cos(i)
pdf = np.cos(inclinations)

# Normalize the PDF to create a probability density
pdf /= np.trapz(pdf, inclinations)  # normalization using trapezoidal integration

# CDF: Cumulative distribution function (integral of PDF)
cdf = np.cumsum(pdf) * (inclinations[1] - inclinations[0])  # discrete integration

# Plot the PDF and CDF
plt.figure(figsize=(12, 6))

# PDF plot
plt.subplot(1, 2, 1)
plt.plot(np.degrees(inclinations), pdf, label='PDF', color='blue')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Probability Density')
plt.title('PDF of Inclination')
plt.legend()

# CDF plot
plt.subplot(1, 2, 2)
plt.plot(np.degrees(inclinations), cdf, label='CDF', color='green')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Inclination')
plt.legend()

plt.tight_layout()
plt.show()
