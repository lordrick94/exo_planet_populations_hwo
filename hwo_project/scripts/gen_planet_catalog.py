import argparse

from hwo_project.planet_simulations import gen_planets, dist_planets_to_stars, make_planet_catalog


def parser():
    parser = argparse.ArgumentParser(description='Generate a catalog of planets around stars.')
    parser.add_argument('--num_planets', type=int, default=30000, help='Number of planets to generate for each star.')
    parser.add_argument('--seed', type=int, default=None, help='Seed for random number generation.')
    parser.add_argument('--show_contrast_plot', action='store_true', help='Show the plot of the contrast vs angular separation.')
    parser.add_argument('--dist_cutoff', type=float, default=None, help='Distance cutoff for stars.')
    return parser


def generate_planet_catalog(num_planets,dist_cutoff,seed):
    # Extract the star data
    from hwo_project.star_data_extraction import star_data_extract
    print('Extracting star data...')
    star_data_extract.extract_star_data(dist_cutoff=dist_cutoff)
    # Generate the planet catalog
    print('Generating planet catalog...')
    gen_planets.gen_random_planets(num_planets, seed)
    # Distribute the planets to stars
    print('Distributing planets to stars...')
    dist_planets_to_stars.run_dist_planets_to_stars(seed=seed)
    # Make the planet catalog
    print('Creating planet catalog...')
    make_planet_catalog.run_create_planet_catalog()


def main():
    # Parse the command line arguments
    args = parser().parse_args()

    # Generate the planet catalog
    generate_planet_catalog(args.num_planets,args.dist_cutoff, args.seed)

    # Show the contrast vs angular separation plot
    if args.show_contrast_plot:
        from hwo_project.plotting import plot_contrast_vs_angular_separation
        plot_contrast_vs_angular_separation.plot_contrast_vs_angular_separation()

if __name__ == "__main__":
    main()



