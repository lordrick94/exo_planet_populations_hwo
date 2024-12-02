from hwo_project.data import data_utils
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load the data
data = data_utils.load_data('star_catalog')

# Bin distances into categories for the violin plot
bins = [0, 5, 10, 25, 50]
data['Distance_Bin'] = pd.cut(data["sy_dist"], bins=bins, labels=[f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)])

# Set the style
sns.set(style="whitegrid")

# Create a violin plot
plt.figure(figsize=(14, 8))
violin_plot = sns.violinplot(
    x="Distance_Bin", 
    y="st_lum", 
    data=data, 
    inner="box", 
    scale="width", 
    palette="coolwarm"
)

# Add annotations for the number of stars in each bin
bin_counts = data['Distance_Bin'].value_counts(sort=False)
for i, count in enumerate(bin_counts):
    plt.text(i, data["st_lum"].min() - 0.5, f"{count}", ha="center", va="top", fontsize=20, color="b")

# Customize the plot
plt.title("Distribution of Luminosities Across Distance Bins", fontsize=24, pad=20)
plt.xlabel("Distance (pc)", fontsize=20, labelpad=15)
plt.ylabel("Luminosity (L☉)", fontsize=20, labelpad=15)
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

# Add a background color to the plot area
violin_plot.set_facecolor('whitesmoke')

# Adjust layout
plt.tight_layout()

# Save the figure with high resolution
plt.savefig(data_utils.get_fig_dir_path() + 'luminosity_violin_plot_presentation.png', dpi=800)

# Show the plot
plt.show()