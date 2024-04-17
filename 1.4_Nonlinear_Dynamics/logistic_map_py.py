import csv
import os
import numpy as np
import time

from logistic_map_cy import compute_bifurcation_optimized, compute_lyapunov_optimized


def logistic_map(x, r):
    return r * x * (1 - x)


def compute_bifurcation(r_values, num_generations, initial_x=0.5, transients=500):
    """Compute bifurcation data."""
    data = []
    for r in r_values:
        x = initial_x
        # Transient iterations
        for _ in range(transients):
            x = logistic_map(x, r)
        # Collect data after transients
        for _ in range(num_generations - transients):
            x = logistic_map(x, r)
            data.append([r, x])
    return data


def compute_lyapunov(r_values, num_generations, initial_x=0.5):
    """Compute Lyapunov exponent data."""
    data = []
    for r in r_values:
        x = initial_x
        lyapunov_sum = 0
        for _ in range(num_generations):
            x = logistic_map(x, r)
            derivative = r * (1 - 2 * x)
            if derivative != 0:
                lyapunov_sum += np.log(abs(derivative))
        data.append([r, lyapunov_sum / num_generations])
    return data


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


if __name__ == '__main__':

    # Define parameters
    r_values = np.linspace(1, 4, 300)
    num_generations = 1000

    # Compute data
    start_time = time.time()
    bifurcation_data = compute_bifurcation(r_values, num_generations)
    end_time = time.time()
    print(f"Python bifurcation calculation time: {end_time - start_time}")

    start_time = time.time()
    lyapunov_data = compute_lyapunov(r_values, num_generations)
    end_time = time.time()
    print(f"Python Lyapunov calculation time: {end_time - start_time}")

    start_time = time.time()
    bifurcation_data_optimized = compute_bifurcation_optimized(
        r_values, num_generations)
    end_time = time.time()
    print(f"Cython bifurcation calculation time: {end_time - start_time}")

    start_time = time.time()
    lyapunov_data_optimized = compute_lyapunov_optimized(
        r_values, num_generations)
    end_time = time.time()
    print(f"Cython Lyapunov calculation time: {end_time - start_time}")

    # Save data
    save_to_csv('bifurcation_data_py.csv', ['r', 'x'], bifurcation_data)
    save_to_csv('lyapunov_data_py.csv', ['r', 'x'], lyapunov_data)

    save_to_csv('bifurcation_data_cy.csv', ['r', 'x'], bifurcation_data)
    save_to_csv('lyapunov_data_cy.csv', ['r', 'x'], lyapunov_data)
