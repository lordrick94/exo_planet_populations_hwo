from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt

# Unequal intervals in x and y
x = np.array([0, 1, 2, 4, 7])
y = np.array([0, 0.5, 1.5, 3])
X, Y = np.meshgrid(x, y)
pdf_values = np.random.rand(len(y), len(x))

# Define a regular grid for interpolation
x_new = np.linspace(x.min(), x.max(), 100)  # Regular x grid
y_new = np.linspace(y.min(), y.max(), 100)  # Regular y grid
X_new, Y_new = np.meshgrid(x_new, y_new)

# Interpolate the PDF values onto the regular grid
pdf_interpolated = griddata(
    (X.ravel(), Y.ravel()), 
    pdf_values.ravel(), 
    (X_new, Y_new), 
    method='cubic'
)

# Plot the interpolated grid
plt.figure(figsize=(8, 6))
plt.imshow(pdf_interpolated, extent=(x.min(), x.max(), y.min(), y.max()), 
           origin='lower', aspect='equal', cmap='viridis')
plt.colorbar(label='PDF Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('PDF on a Regular Grid')
plt.show()
