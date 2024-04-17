import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_results(file_path, label):
    df = pd.read_csv(os.path.join("1.2_Numerical_Integration\data", file_path))
    plt.plot(df['x'], df['Trapezoid'], label=f'Trapezoid {label}')
    plt.plot(df['x'], df['Simpson'], label=f'Simpson {label}')
    plt.plot(df['x'], df['Actual J0'],
             label=f'Actual J0 {label}', linestyle='--')


def plot_relative_errors(file_path, label):
    df = pd.read_csv(os.path.join("1.2_Numerical_Integration\data", file_path))
    plt.loglog(df['N'], df['Relative Error Trapezoid'],
               label=f'Trapezoid {label}', marker='o')
    plt.loglog(df['N'], df['Relative Error Simpson'],
               label=f'Simpson {label}', marker='x')


def plot_function_behavior():
    x_values = [0, 2.5, 5, 7.5, 10]
    theta = np.linspace(0, np.pi, 400)
    for x in x_values:
        f_values = np.cos(x * np.sin(theta))
        plt.plot(theta, f_values, label=f'x={x}')


# Plot integration results
plt.figure(figsize=(10, 6))
# plot_results("numerical_integration_cpp.csv", "C++")
plot_results("numerical_integration_python.csv", "Python")
plot_results("numerical_integration_cython.csv", "Cython")
plt.title("Numerical Integration Comparison")
plt.xlabel("$x$")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# Plot relative errors
plt.figure(figsize=(10, 6))
plot_relative_errors("relative_errors_python.csv", "Python")
plot_relative_errors("relative_errors_cython.csv", "Cython")
# plt.title('Relative Errors of Numerical Integration Methods at $x = 3.83171$')
plt.xlabel('Number of Steps ($N$)')
plt.ylabel('Relative Error')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# Plot function behavior
plt.figure(figsize=(10, 6))
plot_function_behavior()
plt.title('Behavior of $f(\\theta) = \\cos(x \\sin(\\theta))$')
plt.xlabel('$\\theta$')
plt.ylabel('$f(\\theta)$')
plt.legend()
plt.grid(True)
plt.show()
