# Script to extract data from HPIC catalog

import pandas as pd

from hwo_project.models import gen_inclinations

# Load catalog

df = pd.read_csv('hpic_data.txt',sep='|')

# Extract relevant columns
my_columns = ['ra','dec','tic_id','sy_dist','sy_disterr','st_lum','st_mass']

# Convert 'tic_id' to string and remove trailing '.0'
df['tic_id'] = 'S'+df['tic_id'].astype(str).str.replace(r'\.0$', '', regex=True)
df = df[my_columns]

# Filter out rows with missing values
final_df = df.dropna()

print(f'Dropped {df.shape[0] - final_df.shape[0]} rows with missing values.')

# Finally, Add a column for the inclination of the star orbits with the generated mock data

final_df['inclination'] = gen_inclinations.generate_mock_i(final_df.shape[0])

# Save to CSV
final_df.to_csv('star_data.csv',index=False)
