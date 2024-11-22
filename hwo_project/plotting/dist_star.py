import matplotlib.pyplot as plt

from hwo_project.data import data_utils


df = data_utils.load_data('star_catalog')

# Plot a histogram of the distance to the stars
plt.figure(figsize=(10, 6))
plt.hist(df['sy_dist'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.xlabel('Distance (parsecs)')
plt.ylabel('Frequency')
plt.title('Histogram of Star Distances')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()