import argparse

from hwo_project.planet_simulations import gen_planets, dist_planets_to_stars, make_planet_catalog


def parser():
    parser = argparse.ArgumentParser(description='Generate a catalog of planets around stars.')
    parser.add_argument('--num_planets', type=int, default=None, help='Number of planets to generate for each star.')
    parser.add_argument('--seed', type=int, default=None, help='Seed for random number generation.')
    parser.add_argument('--show_contrast_plot', action='store_true', help='Show the plot of the contrast vs angular separation.')
    return parser


def generate_planet_catalog(num_planets, seed):
    # Generate the planet catalog
    gen_planets.gen_random_planets(num_planets, seed)
    # Distribute the planets to stars
    dist_planets_to_stars.run_dist_planets_to_stars(seed=seed)
    # Make the planet catalog
    make_planet_catalog.run_create_planet_catalog()


def main():
    # Parse the command line arguments
    args = parser().parse_args()

    # Generate the planet catalog
    generate_planet_catalog(args.num_planets, args.seed)

    # Show the contrast vs angular separation plot
    if args.show_contrast_plot:
        from hwo_project.plotting import plot_contrast_vs_angular_separation
        plot_contrast_vs_angular_separation.plot_contrast_vs_angular_separation()

if __name__ == "__main__":
    main()



