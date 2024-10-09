import numpy as np

class Star:
    def __init__(self, ra, dec):
        """
        Initialize a star object.

        :param ra: Right ascension of the star (in hexadecimal without ':').
        :param dec: Declination of the star (in hexadecimal without ':').

        """
        self.ra = ra
        self.dec = dec
        self.name = f"S{ra}_{dec}"

    def __str__(self):
        return f"Star {self.name} at RA {self.ra} and Dec {self.dec}."


class Planet:
    def __init__(self, radius, semi_major_axis, albedo, star):
        """
        Initialize a planet object.

        :param name: Name of the planet.
        :param mass: Mass of the planet (in Earth masses).
        :param radius: Radius of the planet (in Earth radii).
        :param semi_major_axis: Semi-major axis of the orbit (in AU).
        :param albedo: Albedo of the planet (fraction of light reflected).
        :param star: The star that the planet orbits (Star object).
        """

        self.radius = radius
        self.albedo = albedo
        self.star = star
        self.name = f"P_{star.name}_{radius}_{albedo}"

    def lambertian_contrast(self):
        """
        Calculate the contrast between the planet and its star using the Lambertian phase function.

        TODO: Implement this method.
        """
        pass

    def __str__(self):
        return f"Planet {self.name} with radius {self.radius} and albedo {self.albedo}."

