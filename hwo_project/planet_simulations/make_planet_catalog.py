from hwo_project.models import obj_models
from hwo_project.data import data_utils

from tqdm import tqdm

from IPython import embed

def create_star_objects(stars_df):
    """
    Create a dictionary of Star objects indexed by their tic_id
    """
    # Create a dictionary of Star objects indexed by their tic_id
    stars_dict = {}
    for _, row in stars_df.iterrows():
        star = obj_models.Star(
            ra=row['ra'],
            dec=row['dec'],
            distance=row['sy_dist'],
            hpic_id=row['tic_id'],
            mass=row['st_mass'],
            inclination=row['inclination'],
            lu_star=row['st_lum']
        )
        stars_dict[row['tic_id']] = star

    return stars_dict


def create_planet_objects(planets_df, stars_dict,verbose=False):
    """
    Create Planet objects and extract the desired attributes
    """
    # Create lists to store the new columns
    contrasts = []
    planet_types = []
    angular_separations = []
    orbital_radii = []
    eff_orbital_radius = []

    # Create Planet objects and extract the desired attributes
    for _, row in tqdm(planets_df.iterrows(), total=len(planets_df), desc="Processing planets"):
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
        eff_orbital_radius.append(planet.eff_radius)

    if verbose:
        print(f"Planet: {planet.name} done.")

    return contrasts, planet_types, angular_separations, orbital_radii, eff_orbital_radius


def add_columns(planets_df,
                contrasts, 
                planet_types, 
                angular_separations, 
                orbital_radii, 
                eff_orbital_radius,
                output_path):
    """
    Add the new columns to the planet DataFrame
    """

    # Add the new columns to the planet DataFrame
    planets_df['contrast'] = contrasts
    planets_df['planet_type'] = planet_types
    planets_df['angular_separation'] = angular_separations
    planets_df['orbital_radius'] = orbital_radii
    planets_df['eff_orbital_radius'] = eff_orbital_radius

    # Save the updated planet DataFrame to a new CSV file
    planets_df.to_csv(output_path, index=False)

    return planets_df



if __name__ == "__main__":
    stars_df = data_utils.load_data('star_catalog')
    planets_df = data_utils.load_data('assigned_planets')

    stars_dict = create_star_objects(stars_df)

    contrasts, planet_types, angular_separations, orbital_radii,eff_radius = create_planet_objects(planets_df, stars_dict)

    output_path = data_utils.load_data('planet_catalog', get_path=True)

    planets_df = add_columns(planets_df, contrasts, planet_types, angular_separations, orbital_radii,eff_radius, output_path)

    print(planets_df.head())



