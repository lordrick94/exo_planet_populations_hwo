import numpy as np
from hwo_project.pdf.v_vs_pdf_model import calc_n_dist

def compute_integral(R=None, P=None):
    """
    Function to compute the double integral of the integrand function over the grid of R and P values.

    Returns:
    integral_values : 2D array of the integral values.
    """
    if R is None or P is None:
        R = np.array([0.67, 1, 1.5, 2.2, 3.4, 5.1, 7.6, 11, 17])
        P = np.array([10, 20, 40, 80, 160, 320, 640]) / 365.25

    integral_values = np.zeros((len(R) - 1, len(P) - 1))

    for i in range(R.shape[0] - 1):
        for j in range(P.shape[0] - 1):
            R_lower = R[i]
            R_upper = R[i + 1]
            P_lower = P[j]
            P_upper = P[j + 1]

            print(f"Making integral grid for R = {R_lower} to {R_upper} earth radiuses and P = {int(P_lower*365.25)} to {int(P_upper*365.25)} days")
            integral_values[i, j] = calc_n_dist.compute_sum(R_lower, R_upper, P_lower, P_upper)
            print(f"Integral value = {integral_values[i, j]}")

    return R, P, integral_values*100

if __name__ == "__main__":
    # Compute the integral values
    R, P, integral_values = compute_integral()
    # Save the integral values to a file
    np.save('r_vs_A_pdf.npy', integral_values)



