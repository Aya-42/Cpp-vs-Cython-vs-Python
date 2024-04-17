import numpy as np
import time
import csv
import os

from scipy.special import j0
from scipy.integrate import simpson, trapezoid

import bessel_cy  # Import the compiled Cython module


def f(theta, x):
    """Calculate the function to be integrated to produce the Bessel function."""
    return np.cos(x * np.sin(theta))


def numerical_integral(x, N):
    """Calculate approximations and actual values of Bessel function for a range of x values."""
    theta = np.linspace(0, np.pi, N+1)
    y = f(theta, x)
    trap_approx = trapezoid(y=y, x=theta)
    simp_approx = simpson(y=y, x=theta)
    return trap_approx, simp_approx


def calculate_relative_errors(x_extremum, N_values):
    """Calculate relative errors for a specific x value."""
    actual_j0_extremum = j0(x_extremum)
    relative_errors_trap = []
    relative_errors_simp = []

    for N in N_values:
        trap_approx, simp_approx = numerical_integral(x_extremum, N)
        rel_error_trap = np.abs(
            (trap_approx - actual_j0_extremum) / actual_j0_extremum)
        rel_error_simp = np.abs(
            (simp_approx - actual_j0_extremum) / actual_j0_extremum)
        relative_errors_trap.append(rel_error_trap)
        relative_errors_simp.append(rel_error_simp)

    return relative_errors_trap, relative_errors_simp


def save_to_csv(filename, header, data, subdirectory="data"):
    """Write data to a CSV file in a specific subdirectory."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the subdirectory path
    target_dir = os.path.join(script_dir, subdirectory)

    # Ensure the directory exists, create if it doesn't
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create the full file path
    file_path = os.path.join(target_dir, filename)

    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


if __name__ == "__main__":

    # Calculate approximations and actual values of Bessel function for a range of x values
    N = 1000
    x_values = np.linspace(0, 10, N+1)

    start_time = time.time()
    data = [[x, *numerical_integral(x, N), j0(x)] for x in x_values]
    end_time = time.time()
    print(f"Python execution time: {end_time - start_time}")

    start_time = time.time()
    data_optimized = [[x, bessel_cy.trapezoid_rule(
        x, N), bessel_cy.simpson_rule(x, N), j0(x)] for x in x_values]
    end_time = time.time()
    print(f"Cython execution time: {end_time - start_time}")

    # Calculate relative errors for specific x value
    x_extremum = 3.83171
    N_values = 10 * 2**np.arange(9)

    start_time = time.time()
    relative_errors_trap, relative_errors_simp = calculate_relative_errors(
        x_extremum, N_values)
    end_time = time.time()
    print(f"Python relative error calculation time: {end_time - start_time}")

    start_time = time.time()
    relative_errors_trap_optimized, relative_errors_simp_optimized = bessel_cy.calculate_relative_errors(
        x_extremum, N_values)
    end_time = time.time()
    print(f"Cython relative error calculation time: {end_time - start_time}")

    # Save data to CSV files
    save_to_csv('numerical_integration_python.csv', [
                'x', 'Trapezoid', 'Simpson', 'Actual J0'], data)

    save_to_csv('numerical_integration_cython.csv', [
                'x', 'Trapezoid', 'Simpson', 'Actual J0'], data_optimized)

    error_data = list(
        zip(N_values, relative_errors_trap, relative_errors_simp))
    save_to_csv('relative_errors_python.csv', [
                'N', 'Relative Error Trapezoid', 'Relative Error Simpson'], error_data)

    error_data_optimized = list(
        zip(N_values, relative_errors_trap_optimized, relative_errors_simp_optimized))
    save_to_csv('relative_errors_cython.csv', [
                'N', 'Relative Error Trapezoid', 'Relative Error Simpson'], error_data_optimized)
