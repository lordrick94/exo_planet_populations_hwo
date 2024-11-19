import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
# Define the angle i in degrees
i_vals = [0, 20, 30, 50, 60, 90]

# Define the range of theta values from 0 to 180 degrees
theta_deg = np.linspace(0, 360, 500)

# Loop over different values of i
for i in i_vals:

    # Convert theta values to radians for calculation
    theta_rad = np.radians(theta_deg)

    # Calculate alpha in radians using the given equation
    alpha_rad = np.arccos(np.sin(np.radians(i)) * np.sin(theta_rad))

    # Convert alpha values to degrees
    alpha_deg = np.degrees(alpha_rad)

    # Plot alpha vs theta
    plt.plot(theta_deg, alpha_deg, label=rf'$i = {i}^\circ$')

# Set up the plot
plt.xlabel(r'$\theta$ (degrees)')
plt.ylabel(r'$\alpha$ (degrees)')
plt.title(r'Plot of $\alpha$ vs $\theta$ for various $i$ values where: $cos \alpha = sin \theta \times sin i$')
plt.xticks(np.arange(0, 361, 45))
plt.yticks(np.arange(0, 181, 30))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.show()