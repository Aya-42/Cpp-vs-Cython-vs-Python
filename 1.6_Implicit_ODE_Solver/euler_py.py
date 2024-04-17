import numpy as np
import time
import csv
import os

from euler_cy import backward_euler_optimized


def backward_euler(y0, t_end, dt):
    times = np.arange(0, t_end + dt, dt)
    ys = np.zeros(len(times))
    ys[0] = y0

    for i in range(1, len(times)):
        ys[i] = ys[i-1] / (1 + dt)

    return times, ys


def analytical_solution(times):
    return np.exp(-times)


def save_to_csv(filename, header, data, subdirectory="data"):
    """Write data to a CSV file in a specific subdirectory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(script_dir, subdirectory)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    file_path = os.path.join(target_dir, filename)
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


# Example usage
y0 = 1
t_end = 16
dt = 0.1

start_time = time.time()
times, ys = backward_euler(y0, t_end, dt)
end_time = time.time()
print("Time taken by Python code:", end_time-start_time)

analytical_ys = analytical_solution(times)
relative_errors = np.abs((ys - analytical_ys) / analytical_ys)
save_to_csv("ode_results_python.csv", ['Time', 'Numerical', 'Analytical', 'Relative Error'], zip(
    times, ys, analytical_ys, relative_errors))


start_time = time.time()
times, ys = backward_euler_optimized(y0, t_end, dt)
end_time = time.time()
print("Time taken by Cython code:", end_time-start_time)
