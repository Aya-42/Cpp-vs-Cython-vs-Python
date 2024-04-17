import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_lorentzian():
    # Read histogram data
    data = pd.read_csv('histogram_data.csv', header=None,
                       names=['bin_edge', 'count'])
    bin_edges = data['bin_edge']
    counts = data['count']

    # Calculate bin centers from bin edges
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Normalize histogram
    bin_width = bin_edges.iloc[1] - bin_edges.iloc[0]
    norm_counts = counts / (sum(counts) * bin_width)

    # Theoretical PDF
    gamma = 1
    x = np.linspace(-10, 10, 1000)
    p_x = (gamma / np.pi) / (gamma**2 + x**2)

    # Plotting
    plt.bar(bin_centers, norm_counts, width=bin_width,
            label='Sampled Distribution')
    plt.plot(x, p_x, 'r-', label='Theoretical PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_lorentzian()
