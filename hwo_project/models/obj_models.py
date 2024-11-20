import numpy as np
from hwo_project import utils

from astropy import units as u, constants as const

class Star:
    def __init__(self, ra, dec, distance, hpic_id, mass, inclination,lu_star):
        """
        Initialize a star object.

        :param ra: Right ascension of the star (in hexadecimal without ':').
        :param dec: Declination of the star (in hexadecimal without ':').
        :param distance: Distance to the star (in parsecs).
        :param hpic_id: HPIC ID of the star.
        :param mass: Mass of the star
        :param inclination: Inclination of the star orbits (in degrees).
        :param lu_star: Luminosity of the star

        """
        self.ra = ra
        self.dec = dec
        self.distance = distance
        self.hpic_id = hpic_id
        self.mass = mass
        self.inclination = inclination
        self.lu_star = lu_star

    def __str__(self):
        return f"Star {self.name} at RA {self.ra} and Dec {self.dec}."


class Planet:
    def __init__(self,planet_name,planet_radius,period, star):
        """
        Initialize a planet object.

        :param planet_name: Name of the planet.
        :param planet_radius: Radius of the planet (in Earth radii).
        :param period: Orbital period of the planet (in days).
        :param star: Star object that the planet orbits.
        """
        self.name = planet_name
        self.radius = planet_radius
        self.star = star
        self.orbital_radius = utils.convert_period_to_orbital_radius(period, star.mass)
        self.optimal_pos = utils.get_optimal_obs_pos(star.inclination)
        self.eff_radius = utils.get_eff_orbital_radius(self.orbital_radius, star.lu_star)
        self.planet_type, self.albedo = utils.get_exoplanet_type(planet_radius,self.eff_radius)

    def angular_separation(self):
        """
        Calculate the angular separation between the planet and its star.
        """
        return utils.get_pos_radius(self.orbital_radius, self.optimal_pos, self.star.inclination)/self.star.distance

    def lambertian_contrast(self):
        """
        Calculate the contrast between the planet and its star using the Lambertian phase function.
        """
        # Convert planet radius from Earth radii to AU
        #p_alpha = utils.calculate_lambertian_phase_function(self.phase_angle) # This is the phase function, we are going to use alpha=60 as constant
        p_alpha = 0.6089977810442295
        contrast = self.albedo * p_alpha *np.pi* utils.convert_earth_radius_to_aus(self.radius) ** 2 / self.orbital_radius ** 2

        return contrast
        

    def __str__(self):
        return f"Planet {self.name} with radius {self.radius} and albedo {self.albedo}."

