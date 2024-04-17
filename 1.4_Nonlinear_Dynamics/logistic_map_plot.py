import os
import pandas as pd
import matplotlib.pyplot as plt


def save_plot(fig, plot_name, directory="plots"):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Save the figure
    fig.savefig(os.path.join(directory, plot_name))
    # Close the figure to free memory
    plt.close(fig)


def plot_bifurcation(filename, show=True, save=False):
    data = pd.read_csv(os.path.join("1.4_Nonlinear_Dynamics\data", filename))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['r'], data['x'], ',k', alpha=0.5)
    ax.set_title('Bifurcation Diagram')
    ax.set_xlabel('r')
    ax.set_ylabel('Steady State x')
    if show:
        plt.show()
    if save:
        save_plot(fig, filename.replace('.csv', '_bifurcation.png'))


def plot_lyapunov(filename, show=True, save=False):
    data = pd.read_csv(os.path.join("1.4_Nonlinear_Dynamics\data", filename))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['r'], data['x'], 'b-', alpha=0.7)
    ax.set_title('Lyapunov Exponents')
    ax.set_xlabel('r')
    ax.set_ylabel('Lyapunov Exponent')
    ax.axhline(0, color='red', lw=0.5, alpha=0.5)
    if show:
        plt.show()
    if save:
        save_plot(fig, filename.replace('.csv', '_lyapunov.png'))


# Plotting
plot_bifurcation('bifurcation_data_py.csv', save=True)
plot_lyapunov('lyapunov_data_py.csv', save=True)

plot_bifurcation('bifurcation_data_cy.csv', save=True)
plot_lyapunov('lyapunov_data_cy.csv', save=True)

plot_bifurcation('bifurcation_data_c.csv', save=True)
plot_lyapunov('lyapunov_data_c.csv', save=True)
