# Functions to calculate various metrics for the model
import numpy as np
import pandas as pd
from astropy import units as u, constants as const

from hwo_project.models import obj_models


def get_optimal_obs_pos(inclination):

    if inclination >30:
        try:
            # Ensure inclination is a valid number
            if not isinstance(inclination, (int, float)):
                raise ValueError("Inclination must be a number.")
            
            # Calculate the angle
            angle = np.arcsin(np.cos(np.radians(60))/np.sin(np.radians(inclination)))
            
            # Check if the result is a valid number
            if np.isnan(angle):
                raise ValueError("Resulting angle is NaN.")
            
            return np.degrees(angle)
        except ZeroDivisionError:
            print("Error: Division by zero encountered.")
            return np.nan
        except ValueError as e:
            print(f"ValueError: {e}")
            return np.nan
        except Exception as e:
            print(f"Unexpected error: {e}")
            return np.nan
        
    elif inclination >= 0 and inclination <= 30:
        return 90
    
    elif inclination > 90:
        print("Warning: Inclination is greater than 90 degrees.")
        return None
    
    else:
        print("Warning: Inclination is less than 0 degrees.")
        return None

def get_pos_radius(radius, phi,inclination):
    """
    Get the position of a planet with a given radius and phase angle.

    :param radius: Radius of the planet (in AU).
    :param phi: Phase angle of the planet (in degrees).
    :param inclination: Inclination of the star orbits (in degrees).
    :return: The position of the planet (in AU).
    """
    return radius * np.sqrt(1 - np.sin(np.radians(phi))**2 * np.cos(np.radians(inclination))**2)


def calculate_lambertian_phase_function(alpha):
    """
    Calculate the phase function for a given phase angle alpha.

    :param alpha: Phase angle (in degrees).
    :return: The phase function value.
    """
    # Convert alpha to radians
    alpha_rad = np.radians(alpha)

    p_alpha = (np.sin(alpha_rad) + (np.pi - alpha_rad) * np.cos(alpha_rad)) / np.pi

    return p_alpha

def convert_period_to_orbital_radius(period, star_mass):
    """
    Convert the period of a planet to its orbital radius around a star.

    :param period: Orbital period of the planet (in days).
    :param star_mass: Mass of the star (in solar masses).
    :return: The orbital radius of the planet (in AU).
    """
    # Convert period to seconds
    period_seconds = (period * u.day.to(u.s))*u.s
    
    # Convert star mass to kg
    star_mass = star_mass * const.M_sun

    # Calculate the orbital radius
    orbital_radius = ((const.G * star_mass * period_seconds**2) / (4 * np.pi**2))**(1/3)

    return (orbital_radius.to(u.AU)).value

def convert_earth_radius_to_aus(earth_radiuses):
    """
    Convert a radius in Earth radii to AU.

    :param earth_radius: Radius in Earth radii.
    :return: Radius in AU.
    """
    return (earth_radiuses * const.R_earth.to(u.AU)).value
    

def create_star_from_tic_id(tic_id, df):
    row = df[df['tic_id'] == tic_id]
    if row.empty:
        raise ValueError(f"TIC ID {tic_id} not found in the DataFrame.")
    
    star = obj_models.Star(
        ra=row['ra'].values[0],
        dec=row['dec'].values[0],
        distance=row['sy_dist'].values[0],
        l_star=row['st_lum'].values[0],
        hpic_id=tic_id,
        mass=row['st_mass'].values[0]
    )
    return star

def get_exoplanet_type(planet_radius, orbital_radius):
    """
    Get the exoplanet type and albedo for a given planet radius and orbital radius.

    :param planet_radius: Radius of the planet (in Earth radii).
    :param orbital_radius: Orbital radius of the planet (in AU).
    :return: The exoplanet type and albedo.
    """

    # Load the CSV file into a DataFrame
    df = pd.read_csv('/home/lordrick/Projects/exo_project/hwo_project/data_extraction/planet_properties.csv')

    for index, row in df.iterrows():
        if (row['planet_radius_lower'] <= planet_radius <= row['planet_radius_upper'] and
            row['orbitals_radius_lower'] <= orbital_radius <= row['orbitals_radius_upper']):
            albedo = np.random.uniform(row['albedo_lower'], row['albedo_upper'])
            return row['exoplanet_type'], albedo
    return None, None