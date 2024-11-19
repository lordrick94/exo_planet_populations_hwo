import pandas as pd

from hwo_project import utils
from hwo_project.models import obj_models

from IPython import embed

# Load the star and planet catalogs into DataFrames
planets_df = pd.read_csv('/home/lordrick/Projects/exo_project/hwo_project/pdf/v_vs_pdf_model/assigned_planets.csv')
stars_df = pd.read_csv('/home/lordrick/Projects/exo_project/hwo_project/data_extraction/star_data.csv')

# Create a dictionary of Star objects indexed by their tic_id
stars_dict = {}
for _, row in stars_df.iterrows():
    star = obj_models.Star(
        ra=row['ra'],
        dec=row['dec'],
        distance=row['sy_dist'],
        hpic_id=row['tic_id'],
        mass=row['st_mass'],
        inclination=row['inclination']
    )
    stars_dict[row['tic_id']] = star

# Create lists to store the new columns
contrasts = []
planet_types = []
angular_separations = []
orbital_radii = []
# Create Planet objects and extract the desired attributes
for _, row in planets_df.iterrows():
    star = stars_dict[row['host_star_id']]
    planet = obj_models.Planet(
        planet_name=row['planet_name'],
        planet_radius=row['planet_radius'],
        period=row['Period(Days)'],
        star=star
    )
    contrasts.append(planet.lambertian_contrast())
    planet_types.append(planet.planet_type)
    angular_separations.append(planet.angular_separation())
    orbital_radii.append(planet.orbital_radius)

    print(f"Planet: {planet.name} done.")

# Add the new columns to the planet DataFrame
planets_df['contrast'] = contrasts
planets_df['planet_type'] = planet_types
planets_df['angular_separation'] = angular_separations
planets_df['orbital_radius'] = orbital_radii

# Save the updated planet DataFrame to a new CSV file
planets_df.to_csv('updated_planets.csv', index=False)

print(planets_df)