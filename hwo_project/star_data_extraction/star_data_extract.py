# Script to extract data from HPIC catalog

import pandas as pd

from hwo_project.planet_simulations import gen_inclinations
from hwo_project.data import data_utils

from IPython import embed
# Load catalog

def extract_star_data(dist_cutoff=None,sep='|',verbose=False):
    df = data_utils.load_data('raw_stars',sep=sep)

    # Extract relevant columns
    my_columns = ['ra','dec','tic_id','sy_dist','sy_disterr','st_lum','st_mass']

    # Convert 'tic_id' to string and remove trailing '.0'
    df['tic_id'] = 'S'+df['tic_id'].astype(str).str.replace(r'\.0$', '', regex=True)
    df = df[my_columns]

    # Filter out rows with missing values
    mod_df = df.dropna()

    if verbose:
        print(f'Dropped {df.shape[0] - mod_df.shape[0]} rows with missing values.')

    # Finally, Add a column for the inclination of the star orbits with the generated mock data

    final_df = mod_df.copy()

    final_df.loc[:,'inclination'] = gen_inclinations.generate_mock_i(final_df.shape[0])

    if dist_cutoff is not None:
        # Filter out stars with distance greater than 30 parsecs
        final_df = final_df[final_df['sy_dist'] <= dist_cutoff]
        if verbose:
            print(f'Dropped {mod_df.shape[0] - final_df.shape[0]} stars with distance greater than {dist_cutoff} parsecs.')

    # Save to CSV
    out_path = data_utils.load_data('star_catalog',get_path=True)
    final_df.to_csv(out_path,index=False)

if __name__ == '__main__':
    extract_star_data(dist_cutoff=30)
    print('Star data extraction complete')
