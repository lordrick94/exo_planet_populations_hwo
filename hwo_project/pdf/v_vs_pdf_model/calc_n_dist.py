import numpy as np
from scipy.integrate import dblquad

# Function to represent the integrand R^alpha_i * P^beta_i
def integrand(ln_P, ln_R, alpha_i, beta_i):
    R = np.exp(ln_R)
    P = np.exp(ln_P)
    return (R**alpha_i) * (P**beta_i)

# Function to evaluate the integral for a given i
def evaluate_integral(R_min, R_max, P_min, P_max, alpha_i, beta_i, Ri, Ri_1, dbg=False):
    if dbg:
        print(f"Computing integral for alpha = {alpha_i}, beta = {beta_i},R_lower = {max(R_min, Ri_1)}, R_upper = {min(R_max, Ri)}")
    # Define the limits for R and P in terms of their logarithms
    lower_ln_R = np.log(max(R_min, Ri_1))
    upper_ln_R = np.log(min(R_max, Ri))
    lower_ln_P = np.log(P_min)
    upper_ln_P = np.log(P_max)

    # Perform the double integral
    result, error = dblquad(
        integrand,              # Function to integrate
        lower_ln_R,             # Lower bound for ln(R)
        upper_ln_R,             # Upper bound for ln(R)
        lambda ln_R: lower_ln_P, # Lower bound for ln(P)
        lambda ln_R: upper_ln_P, # Upper bound for ln(P)
        args=(alpha_i, beta_i)   # Additional arguments passed to integrand
    )
    
    return result

# Function to compute the sum over i=1 and i=2
def compute_sum(R_min, R_max, P_min, P_max, dbg=False):
    total_sum = 0
    # Constants
    # Parameters for i=1 and i=2
    alpha_list = [-0.19, -1.18]  # alpha_1 = -0.19, alpha_2 = -1.18
    beta_list = [0.26, 0.59]   # beta_1 = 0.26, beta_2 = 0.59
    R_i_list = [3.4, np.inf]    # R_1 = 0.34, R_2 = 1000000
    gamma_list = [0.38, 0.73] # gamma_1 = 0.38, gamma_2 = 0.73

    for i in range(1, 3):  # i = 1, 2
        Ri = R_i_list[i-1]      # R_i for the current i
        Ri_1 = R_i_list[i-2] if i > 1 else R_min  # R_{i-1}, R_min for i=1
        alpha_i = alpha_list[i-1]  # alpha_i for the current i
        beta_i = beta_list[i-1]    # beta_i for the current i
        gamma_i = gamma_list[i-1] # gamma_i for the current i
        
        # Evaluate the integral for the current i
        integral_result = gamma_i*evaluate_integral(R_min, R_max, P_min, P_max, alpha_i, beta_i, Ri, Ri_1)

        if integral_result < 0:
            integral_result = 0
        if dbg:
            # Print the result for the current i
            print(f"Integral result for i = {i}: {integral_result}")
        
        # Sum up the result
        total_sum += integral_result
    
    return total_sum


if __name__ == "__main__":
    # Example values for constants
    R_min = 1
    R_max = 15
    P_min = 41/365.25
    P_max = 72/365.25


    # Compute the total sum
    total_result = compute_sum(R_min, R_max, P_min, P_max)
    print(f"The total sum of the integrals is: {total_result}")
