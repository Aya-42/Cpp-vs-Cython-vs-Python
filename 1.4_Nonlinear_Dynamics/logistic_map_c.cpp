#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <chrono>
#include "utils.h"

// Logistic map function
double logistic_map(double x, double r)
{
    return r * x * (1 - x);
}

// Compute bifurcation data
std::vector<std::pair<double, double>> compute_bifurcation(const std::vector<double> &r_values, int num_generations, double initial_x = 0.5, int transients = 500)
{
    std::vector<std::pair<double, double>> data;
    for (double r : r_values)
    {
        double x = initial_x;
        // Transient iterations
        for (int i = 0; i < transients; ++i)
        {
            x = logistic_map(x, r);
        }
        // Collect data after transients
        for (int i = 0; i < num_generations - transients; ++i)
        {
            x = logistic_map(x, r);
            data.emplace_back(r, x);
        }
    }
    return data;
}

// Compute Lyapunov exponent data
std::vector<std::pair<double, double>> compute_lyapunov(const std::vector<double> &r_values, int num_generations, double initial_x = 0.5)
{
    std::vector<std::pair<double, double>> data;
    for (double r : r_values)
    {
        double x = initial_x;
        double lyapunov_sum = 0.0;
        for (int i = 0; i < num_generations; ++i)
        {
            x = logistic_map(x, r);
            double derivative = r * (1 - 2 * x);
            if (derivative != 0)
            {
                lyapunov_sum += std::log(std::abs(derivative));
            }
        }
        data.emplace_back(r, lyapunov_sum / num_generations);
    }
    return data;
}

int main()
{
    // Generate r values
    std::vector<double> r_values = linspace(1.0, 4.0, 300);

    // Timing bifurcation computation
    auto start = std::chrono::high_resolution_clock::now();
    auto bifurcation_data = compute_bifurcation(r_values, 1000);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << "Bifurcation calculation time: " << diff.count() << " s\n";

    // Timing Lyapunov computation
    start = std::chrono::high_resolution_clock::now();
    auto lyapunov_data = compute_lyapunov(r_values, 1000);
    end = std::chrono::high_resolution_clock::now();
    diff = end - start;
    std::cout << "Lyapunov calculation time: " << diff.count() << " s\n";

    // Save results
    save_to_csv("bifurcation_data_c.csv", bifurcation_data, "r,x");
    save_to_csv("lyapunov_data_c.csv", lyapunov_data, "r,x");
    return 0;
}