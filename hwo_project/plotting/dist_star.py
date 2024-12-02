import matplotlib.pyplot as plt
import seaborn as sns
from hwo_project.data import data_utils

# Load the data
df = data_utils.load_data('star_catalog')

# Set the style
sns.set(style="dark")

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Plot the histogram
sns.histplot(df['sy_dist'], bins=30, kde=False, color='skyblue', edgecolor='black', alpha=0.7)

# Calculate mean and median
mean_dist = df['sy_dist'].mean()
median_dist = df['sy_dist'].median()

# Add labels and title with larger font sizes
plt.xlabel('Distance (parsecs)', fontsize=24)
plt.ylabel('Frequency', fontsize=24)
plt.title('Histogram of Star Distances', fontsize=18)

# Add a legend
plt.legend(fontsize=24)

# Add grid with specific style
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Save the figure with high resolution
plt.savefig(data_utils.get_fig_dir_path() + 'dist_star_presentation.png', dpi=800)

# Show the plot
plt.show()