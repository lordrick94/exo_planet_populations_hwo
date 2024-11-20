import pandas as pd

from astropy import units as u

from hwo_project.data import data_utils

def get_num_observable_planets(planets_df,telescope_constraints_dict=None,telescope_type='hwo',exoplanet_type='earths'):
    """
    Get the number of observable planets in the planet DataFrame
    """

    if telescope_constraints_dict:
        tele_dict = telescope_constraints_dict

    else:
        tele_dict = data_utils.load_data('tele_constraints')

    contrast_cut = planets_df['contrast'] > tele_dict[telescope_type]['contrast_floor']
    angular_separation_cut = planets_df['angular_separation'] > tele_dict[telescope_type]['iwa']
    mod_df = planets_df[contrast_cut & angular_separation_cut]
    mask = mod_df['planet_type'] == exoplanet_type
    return len(mod_df[mask])