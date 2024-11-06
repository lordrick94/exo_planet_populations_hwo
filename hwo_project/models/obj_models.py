import numpy as np
from hwo_project import utils

from astropy import units as u

class Star:
    def __init__(self, ra, dec, distance,l_star, hpic_id, mass):
        """
        Initialize a star object.

        :param ra: Right ascension of the star (in hexadecimal without ':').
        :param dec: Declination of the star (in hexadecimal without ':').
        :param distance: Distance to the star (in parsecs).
        :param l_star: Luminosity of the star (in solar luminosities).

        """
        self.ra = ra
        self.dec = dec
        self.distance = distance
        self.l_star = l_star
        self.hpic_id = hpic_id
        self.mass = mass
        self.name = f"S{ra}_{dec}"

    def __str__(self):
        return f"Star {self.name} at RA {self.ra} and Dec {self.dec}."


class Planet:
    def __init__(self, planet_radius,period, albedo,phase_angle, star):
        """
        Initialize a planet object.

        :param name: Name of the planet.
        :param mass: Mass of the planet (in Earth masses).
        :param radius: Radius of the planet (in Earth radii).
        :param semi_major_axis: Semi-major axis of the orbit (in AU).
        :param albedo: Albedo of the planet (fraction of light reflected).
        :param phase_angle: Phase angle of the planet (in degrees).
        :param star: The star that the planet orbits (Star object).
        """

        self.radius = planet_radius
        self.albedo = albedo
        self.phase_angle = phase_angle
        self.star = star
        self.orbital_radius = utils.convert_period_to_orbital_radius(period, star.mass)
        self.name = f"P_{star.name}_{planet_radius}_{albedo}"

    def lambertian_contrast(self):
        """
        Calculate the contrast between the planet and its star using the Lambertian phase function.
        """
        # Convert planet radius from Earth radii to AU
        p_alpha = utils.calculate_lambertian_phase_function(self.phase_angle)
        contrast = self.albedo * p_alpha *np.pi* utils.convert_earth_radius_to_aus(self.radius) ** 2 / self.orbital_radius ** 2

        return contrast
        

    def __str__(self):
        return f"Planet {self.name} with radius {self.radius} and albedo {self.albedo}."

