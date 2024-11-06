# Script to extract data from HPIC catalog

import pandas as pd

# Load catalog

df = pd.read_csv('hpic_data.txt',sep='|')

# Extract relevant columns
my_columns = ['ra','dec','tic_id','sy_dist','sy_disterr','st_lum','st_mass']

df = df[my_columns]

# Filter out rows with missing values
final_df = df.dropna()

print(f'Dropped {df.shape[0] - final_df.shape[0]} rows with missing values.')

# Save to CSV
final_df.to_csv('star_data.csv',index=False)
