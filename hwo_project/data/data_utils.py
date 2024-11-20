import os
import importlib.resources as pkg_resources
import pandas as pd
import numpy as np
import json

# Load the data
def load_data(filename='planet_catalog', get_path=False):
    # Define the mapping of filenames to their respective paths
    data_paths = {
        'planet_catalog': os.path.join(pkg_resources.files('hwo_project'), 'data/updated_planets.csv'),
        'random_planets': os.path.join(pkg_resources.files('hwo_project'), 'data/random_planets.csv'),
        'assigned_planets': os.path.join(pkg_resources.files('hwo_project'), 'data/assigned_planets.csv'),
        'planet_properties': os.path.join(pkg_resources.files('hwo_project'), 'data/planet_properties.csv'),
        'star_catalog': os.path.join(pkg_resources.files('hwo_project'), 'data/star_data.csv'),
        'pdf_grid': os.path.join(pkg_resources.files('hwo_project'), 'planet_simulations/pdf/r_vs_A_pdf_final.npy'),
        'tele_constraints': os.path.join(pkg_resources.files('hwo_project'), 'data/telescope_constraints.json')
    }

    # Get the data path based on the filename
    data_path = data_paths.get(filename)

    if data_path is None:
        print('No data found for filename:', filename)
        return None

    # Load the data based on the file extension
    if data_path.endswith('.csv'):
        data = pd.read_csv(data_path)
    elif data_path.endswith('.npy'):
        data = np.load(data_path)
    elif data_path.endswith('.json'):
        with open(data_path, 'r') as f:
            data = json.load(f)
    else:
        print('Data format not supported.')
        return None

    if get_path:
        return data_path
    else:
        return data

def quick_catalog_load():
    """
    Quick load the data for the project.
    """
    # Load the planet catalog
    planet_catalog = load_data('planet_catalog')
    # Load the star catalog
    star_catalog = load_data('star_catalog')


    return planet_catalog, star_catalog

def get_fig_dir_path():
    return os.path.join(pkg_resources.files('hwo_project'), 'figures/')