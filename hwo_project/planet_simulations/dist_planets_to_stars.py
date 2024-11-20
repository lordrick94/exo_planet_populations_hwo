import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from hwo_project.data import data_utils

from IPython import embed

def generate_planets_per_star(num_stars, 
                              total_planets, 
                              max_planets_per_star, 
                              min_planets_per_star,
                              seed=None,
                              expected_planets_per_star=None, show_plot=False):
    """
    Function to generate the number of planets for each star based on the occurrence rate distribution.

    Returns:
    planets_per_star : Array of the number of planets for each star.
    """

    if expected_planets_per_star is None:

        pdf_from_sag13 = np.array([[0.001, 0.02, 0.04, 0.07, 0.11, 0.17],
                                [0.335, 0.527, 0.73, 0.92, 1.12, 2.72],
                                [0.85, 1.28, 1.94, 2.92, 3.6, 5.0],
                                [1.35, 2.14, 3.89, 5.93, 7.75, 9.29],
                                [3.55, 5.85, 7.96, 9.74, 12.08, 13.88]])
        

        # Calculate the expected number of planets per star
        expected_planets_per_star = np.sum(pdf_from_sag13) / 100

    if seed is not None:
        np.random.seed(seed)


    # Simulate the number of planets for each star using a Poisson distribution
    planets_per_star = np.random.poisson(lam=expected_planets_per_star, size=num_stars)

    # Ensure every star has at least one planet
    planets_per_star = np.maximum(planets_per_star, min_planets_per_star)

    # Cap the planets per star to the maximum allowed (7)
    planets_per_star = np.minimum(planets_per_star, max_planets_per_star)

    # Ensure the total number of planets does not exceed the given limit
    cumulative_planets = np.cumsum(planets_per_star)
    print("Total Number of Planets assigned to stars:", cumulative_planets[-1])

    cutoff_index = np.searchsorted(cumulative_planets, total_planets, side='right')

    # Adjust the planets per star to not exceed the total number of planets
    if cutoff_index < num_stars:
        planets_per_star[cutoff_index] = total_planets - cumulative_planets[cutoff_index - 1]
        planets_per_star[cutoff_index + 1:] = 0

    if show_plot:
        # Plot the distribution of planets per star
        plt.hist(planets_per_star, bins=range(max_planets_per_star + 2), edgecolor='black')
        plt.title(f'Distribution of Planets per Star\nTotal Planets: {cumulative_planets[-1]}\nExpected Planets per Star: {expected_planets_per_star}\nNumber of Stars: {num_stars}')
        plt.xlabel('Number of Planets')
        plt.ylabel('Number of Stars')

        fig_dir = data_utils.get_fig_dir_path()
        plt.savefig(fig_dir+'planets_per_star.png')
        plt.show()

    return planets_per_star

def assign_planets_to_stars(planets_per_star,num_total_planets,seed=None ,demo=False):
    """
    Function to assign planets to stars based on the number of planets for each star.

    Returns:
    planet_indices : List of lists containing the indices of planets assigned to each star.
    """

    planet_indices = []

    planet_list = list(range(num_total_planets))

    if seed is not None:
        np.random.seed(seed)

    np.random.shuffle(planet_list)

    start_index = 0

    for num_planets in planets_per_star:
        end_index = start_index + num_planets
        planet_indices.append(planet_list[start_index:end_index])
        start_index = end_index


    if demo:
        print("Example of planets assigned to the first 5 stars:")
        for i in range(100):
            print(f"Star {i + 1}: {planet_indices[i]}")

    return planet_indices

def assign_star_ids_to_planets(planets_df, stars_df, planet_indices):
    """
    Assign star IDs to planets based on the provided indices.

    :param planets_df: DataFrame containing the planet data.
    :param stars_df: DataFrame containing the star data.
    :param planet_indices: List of lists containing the indices of planets assigned to each star.
    :return: Updated DataFrame with a new column 'star_id' indicating the host star for each planet.
    """
    if len(planets_df) < len(stars_df):
        print('Warning: Number of planets is less than the number of stars. Some stars will not have any planets assigned.')
    # Initialize the 'host_star_id' column with NaN values
    planets_df['host_star_id'] = 'unlucky'


    # Convert the 'host_star_id' column to string dtype
    planets_df['host_star_id'] = planets_df['host_star_id'].astype(str)

    # Assign star IDs to the specified planet indices
    for star_index, planet_list in enumerate(planet_indices):
        star_id = str(stars_df.iloc[star_index]['tic_id'])  # Ensure star_id is a string
        for planet_index in planet_list:
            planets_df.at[planet_index, 'host_star_id'] = star_id

    # Remove any rows with host_star_id 'unlucky'
    planets_df = planets_df[planets_df['host_star_id'] != 'unlucky']


    

    return planets_df

def add_name_ids_to_planets(planets_df):
    """
    Add a unique name ID to each planet in the DataFrame.

    :param planets_df: DataFrame containing the planet data.
    :return: Updated DataFrame with a new column 'planet_name' indicating the name ID of each planet.
    """
    planet_names = [f"Planet_{i + 1}" for i in range(len(planets_df))]

    mod_df = planets_df.copy()
    mod_df['planet_name'] = planet_names

    return mod_df

def run_dist_planets_to_stars(show_plot=False,seed=None):

    
    # Load the star and planet DataFrames
    _, star_df = data_utils.quick_catalog_load()
    planet_df = data_utils.load_data('random_planets')

    # Given values
    num_stars = len(star_df)  # Number of stars
    total_planets = len(planet_df)  # Updated total number of planets
    max_planets_per_star = 7
    min_planets_per_star = 1

    # Generate the number of planets for each star
    planets_per_star = generate_planets_per_star(num_stars, total_planets, max_planets_per_star, min_planets_per_star, show_plot=show_plot,seed=seed)

    # Get the indices of planets assigned to each star
    planet_indices = assign_planets_to_stars(planets_per_star,total_planets,seed=seed, demo=False)

    # Assign star IDs to planets
    updated_planet_df = assign_star_ids_to_planets(planet_df, star_df, planet_indices)

    # Add unique name IDs to planets
    updated_planet_df = add_name_ids_to_planets(updated_planet_df)

    # Save the updated DataFrame to a CSV file
    out_path = data_utils.load_data('assigned_planets', get_path=True)
    updated_planet_df.to_csv(out_path, index=False)

if __name__ == "__main__":
    run_dist_planets_to_stars(show_plot=False)

