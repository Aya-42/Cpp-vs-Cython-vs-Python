from tracemalloc import start
import numpy as np
import csv
import os
import time

from lorentzian_sampling_cy import lorentzian_transform_optimized


def lorentzian_transform(u, gamma=1):
    return gamma / np.tan(np.pi * (u - 0.5))


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
    n = 100000000  # Number of samples
    random_uniform = np.random.rand(n)

    start = time.time()
    transformed_samples = lorentzian_transform(random_uniform)
    print(f"Python Time Taken: {time.time() - start}")

    start = time.time()
    transformed_samples_optimized = lorentzian_transform_optimized(
        random_uniform)
    print(f"Cython Time taken: {time.time() - start}")

    # Create a histogram of the sampled values
    counts, bin_edges = np.histogram(
        transformed_samples, bins=1000, range=[-10, 10])
    histogram_data = list(zip(bin_edges[:-1], counts))

    # Save histogram data to a CSV file
    save_to_csv('histogram_data_py.csv', ['bin_edge', 'count'], histogram_data)
