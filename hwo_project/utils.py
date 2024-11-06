# Functions to calculate various metrics for the model
import numpy as np
from astropy import units as u, constants as const


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

def calculate_star_planet_angular_separation(orbital_radius, star_distance):
    """
    Calculate the angular separation between a star and a planet.

    :param orbital_radius: Orbital radius of the planet (in AU).
    :param star_distance: Distance to the star (in parsecs).
    :return: The angular separation between the star and the planet (in arseconds).
    """
    # Convert orbital radius to parsecs
    orbital_radius_pc = (orbital_radius*u.AU).to(u.pc)

    # Calculate the angular separation
    angular_separation = np.degrees(np.arctan(orbital_radius_pc / (star_distance*u.pc))) * 3600

    return angular_separation* u.arcsec

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

    return orbital_radius.to(u.AU)

def convert_earth_radius_to_aus(earth_radiuses):
    """
    Convert a radius in Earth radii to AU.

    :param earth_radius: Radius in Earth radii.
    :return: Radius in AU.
    """
    return earth_radiuses * const.R_earth.to(u.AU)
    

