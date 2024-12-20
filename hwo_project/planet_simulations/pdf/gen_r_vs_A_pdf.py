import numpy as np
from hwo_project.planet_simulations.pdf import calc_n_dist

from tqdm import tqdm

def compute_integral(R=None,P=None,dbg=False):
    """
    Function to compute the double integral of the integrand function over the grid of R and P values.

    Returns:
    integral_values : 2D array of the integral values.
    """
    if R is None:
        R = np.array([0.67, 1, 1.5, 2.2, 3.4, 5.1, 7.6, 11, 17])

    if P is None:
        P = np.array([10, 20, 40, 80, 160, 320, 640]) / 365.25

    integral_values = np.zeros((len(R) - 1, len(P) - 1))

    total_iterations = (R.shape[0] - 1) * (P.shape[0] - 1)
    with tqdm(total=total_iterations, desc="Computing integrals") as pbar:
        for i in range(R.shape[0] - 1):
            for j in range(P.shape[0] - 1):
                R_lower = R[i]
                R_upper = R[i + 1]
                P_lower = P[j]
                P_upper = P[j + 1]

                if dbg:
                    print(f"Making integral grid for R = {R_lower} to {R_upper} earth radiuses and P = {int(P_lower*365.25)} to {int(P_upper*365.25)} days")
                integral_values[i, j] = calc_n_dist.compute_sum(R_lower, R_upper, P_lower, P_upper)
                if dbg:
                    print(f"Integral value = {integral_values[i, j]}")

                pbar.update(1)

    return R, P, integral_values

if __name__ == "__main__":
    # Compute the integral values
    R = np.arange(0.67, 17.1, 0.1)
    P = np.arange(10, 640, 1) / 365.25
    R, P, integral_values = compute_integral(R,P)
    # Save the integral values to a file
    np.save('r_vs_A_pdf_final.npy', integral_values)



