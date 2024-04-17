import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_errors(filename):
    data = pd.read_csv(os.path.join("1.6_Implicit_ODE_Solver\data", filename))
    plt.figure(figsize=(10, 6))
    plt.semilogy(data['Time'], data['Relative Error'], label='Relative Error')
    plt.title('Log of Relative Error over Time')
    plt.xlabel('Time')
    plt.ylabel('Log of Relative Error')
    plt.legend()
    plt.grid(True)
    plt.show()


plot_errors('ode_results_python.csv')
