import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from hwo_project.data import data_utils

df = data_utils.load_data("planet_properties")

fig, ax = plt.subplots(figsize=(12, 8))

lower_bound_y = df['planet_radius_lower']
upper_bound_y = df['planet_radius_upper']

lower_bound_x = df['orbitals_radius_lower']
upper_bound_x = df['orbitals_radius_upper']

albedo_range_upper = df['albedo_upper']
albedo_range_lower = df['albedo_lower']

text = df['exoplanet_type']

# Define a colormap
cmap = plt.get_cmap("viridis") 

norm = mcolors.Normalize(vmin=0, vmax=len(df))

for i in range(len(df)):
    color = cmap(norm(i))
    ax.fill_betweenx([lower_bound_y[i], upper_bound_y[i]], lower_bound_x[i], upper_bound_x[i], color=color, alpha=0.5)
    mid_x = (lower_bound_x[i] + upper_bound_x[i]) / 2
    mid_y = (lower_bound_y[i] + upper_bound_y[i]) / 2
    ax.text(mid_x, mid_y, text[i], fontsize=12, ha='center', va='center', color='black', weight='bold')

ax.set_xlabel(r'Orbital Radius $\times \frac{L}{L_{\odot}}$ (AU)', fontsize=24)
ax.set_ylabel('Planet Radius (R⊕)', fontsize=20)
ax.set_xlim(0, 3)
ax.set_title('Exoplanet Properties', fontsize=20)
ax.grid(True, linestyle='--', alpha=0.7)

# Custom legend
handles = [plt.Line2D([0], [0], color=cmap(norm(i)), lw=4, alpha=0.5) for i in range(len(df))]
labels = [f'{text[i]}: Albedo {albedo_range_lower[i]} - {albedo_range_upper[i]}' for i in range(len(df))]
ax.legend(handles, labels, fontsize=14, loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout(rect=[0, 0, 0.95, 1])

plt.savefig(data_utils.get_fig_dir_path()+'exoplanet_properties.png')
plt.show()