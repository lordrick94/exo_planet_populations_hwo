import numpy as np
import matplotlib.pyplot as plt


def generate_planets_per_star(num_stars, total_planets, expected_planets_per_star, max_planets_per_star, min_planets_per_star, show_plot=False):
    """
    Function to generate the number of planets for each star based on the occurrence rate distribution.

    Returns:
    planets_per_star : Array of the number of planets for each star.
    """


    # Simulate the number of planets for each star using a Poisson distribution
    planets_per_star = np.random.poisson(lam=expected_planets_per_star, size=num_stars)

    # Ensure every star has at least one planet
    planets_per_star = np.maximum(planets_per_star, min_planets_per_star)

    # Cap the planets per star to the maximum allowed (7)
    planets_per_star = np.minimum(planets_per_star, max_planets_per_star)

    # Ensure the total number of planets does not exceed the given limit
    cumulative_planets = np.cumsum(planets_per_star)
    print("Total Number of Planets:", cumulative_planets[-1])

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
        plt.show()

    return planets_per_star

def assign_planets_to_stars(planets_per_star,num_total_planets, demo=False):
    """
    Function to assign planets to stars based on the number of planets for each star.

    Returns:
    planet_indices : List of lists containing the indices of planets assigned to each star.
    """

    planet_indices = []

    planet_list = list(range(num_total_planets))

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


if __name__ == "__main__":
    pdf_from_sag13 = np.array([[0.001, 0.02, 0.04, 0.07, 0.11, 0.17],
                                [0.335, 0.527, 0.73, 0.92, 1.12, 2.72],
                                [0.85, 1.28, 1.94, 2.92, 3.6, 5.0],
                                [1.35, 2.14, 3.89, 5.93, 7.75, 9.29],
                                [3.55, 5.85, 7.96, 9.74, 12.08, 13.88]])


    # Given values
    num_stars = 13000
    total_planets = 50000  # Updated total number of planets
    expected_planets_per_star = np.sum(pdf_from_sag13) / 100
    max_planets_per_star = 7
    min_planets_per_star = 1

    # Generate the number of planets for each star
    planets_per_star = generate_planets_per_star(num_stars, total_planets, expected_planets_per_star, max_planets_per_star, min_planets_per_star, show_plot=True)

    # Assign planets to stars
    planet_indices = assign_planets_to_stars(planets_per_star,total_planets, demo=True)

