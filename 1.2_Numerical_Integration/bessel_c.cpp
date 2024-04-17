#define _USE_MATH_DEFINES

#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include "utils.h"
#include <iomanip>

// Function to calculate the integrand for Bessel function calculation
double f(double theta, double x)
{
    return std::cos(x * std::sin(theta));
}

// Perform numerical integration using Trapezoidal rule
double trapezoid_rule(const std::vector<double> &y, const std::vector<double> &x)

{
    double sum = 0.0;
    for (size_t i = 0; i < x.size() - 1; ++i)
    {
        sum += (y[i] + y[i + 1]) * (x[i + 1] - x[i]) / 2.0;
    }
    return sum;
}

// Perform numerical integration using Simpson's rule
double simpson_rule(const std::vector<double> &y, const std::vector<double> &x)
{
    double sum = y.front() + y.back();
    for (size_t i = 1; i < x.size() - 1; i++)
    {
        sum += y[i] * (i % 2 == 0 ? 2 : 4);
    }
    return sum * (x[1] - x[0]) / 3.0;
}

// Function to calculate relative errors
std::vector<std::vector<double>> calculate_relative_errors(double x_extremum, const std::vector<int> &N_values)
{
    std::vector<std::vector<double>> errors;

    double actual_j0_extremum = std::cyl_bessel_j(0, x_extremum);
    for (int N : N_values)
    {
        std::vector<double> theta(N + 1), y(N + 1);
        for (int j = 0; j <= N; ++j)
        {
            theta[j] = j * M_PI / N;
            y[j] = f(theta[j], x_extremum);
        }
        double trap_approx = trapezoid_rule(y, theta);
        double simp_approx = simpson_rule(y, theta);
        double rel_error_trap = std::abs((trap_approx - actual_j0_extremum) / actual_j0_extremum);
        double rel_error_simp = std::abs((simp_approx - actual_j0_extremum) / actual_j0_extremum);
        errors.push_back({static_cast<double>(N), rel_error_trap, rel_error_simp});
    }
    return errors;
}

// Main function integrating all components
int main()
{
    const int N = 1000;
    std::vector<double> x_values = linspace(0, 10, N + 1);
    std::vector<std::vector<double>> data(N + 1);

    auto start_time = std::chrono::high_resolution_clock::now();

    for (int i = 0; i <= N; ++i)
    {
        double x = x_values[i];
        std::vector<double> theta = linspace(0, M_PI, N + 1);
        std::vector<double> y(N + 1);
        for (int j = 0; j <= N; ++j)
        {
            y[j] = f(theta[j], x);
        }
        double trap = trapezoid_rule(y, theta);
        double simp = simpson_rule(y, theta);
        double actual_j0 = std::cyl_bessel_j(0, x); // Standard C++17 Bessel function
        data[i] = {x, trap, simp, actual_j0};
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    std::cout << "Execution time: " << elapsed.count() << " seconds" << std::endl;

    save_to_csv("numerical_integration_cpp.csv", {"x,Trapezoid,Simpson,Actual J0"}, data);

    // Error analysis and saving using the same save function
    std::vector<int> N_values = {10, 20, 40, 80, 160, 320, 640, 1280, 2560};
    double x_extremum = 3.83171;
    std::vector<std::vector<double>> error_data = calculate_relative_errors(x_extremum, N_values);
    save_to_csv("relative_errors_cpp.csv", {"N,Relative Error Trapezoid,Relative Error Simpson"}, error_data);

    return 0;
}
