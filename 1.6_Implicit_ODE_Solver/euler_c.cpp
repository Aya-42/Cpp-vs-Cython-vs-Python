#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <chrono>
#include "utils.h"

std::vector<double> backward_euler(double y0, double t_end, double dt)
{
    size_t num_steps = static_cast<size_t>(t_end / dt) + 1;
    std::vector<double> ys(num_steps);
    ys[0] = y0;
    double factor = 1.0 / (1.0 + dt);
    for (size_t i = 1; i < num_steps; ++i)
    {
        ys[i] = ys[i - 1] * factor;
    }
    return ys;
}

std::vector<double> analytical_solution(const std::vector<double> &times)
{
    std::vector<double> analytical_ys;
    for (double time : times)
    {
        analytical_ys.push_back(std::exp(-time));
    }
    return analytical_ys;
}

int main()
{
    double y0 = 1.0, t_end = 16.0, dt = 0.001;

    int num_points = static_cast<int>(t_end / dt) + 1;
    auto times = linspace(0, t_end, num_points);

    auto start_time = std::chrono::steady_clock::now();
    std::vector<double> ys = backward_euler(y0, t_end, dt);
    auto end_time = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end_time - start_time;
    std::cout << "Time taken by C++ code: " << elapsed_seconds.count() << "s" << std::endl;

    std::vector<double> analytical_ys = analytical_solution(times);
    std::vector<double> relative_errors(times.size());
    for (size_t i = 0; i < times.size(); ++i)
    {
        relative_errors[i] = std::abs((ys[i] - analytical_ys[i]) / analytical_ys[i]);
    }

    std::vector<std::vector<double>> results;
    for (size_t i = 0; i < times.size(); ++i)
    {
        results.push_back({times[i], ys[i], analytical_ys[i], relative_errors[i]});
    }

    save_to_csv("ode_results_cpp.csv", {"Time", "Numerical", "Analytical", "Relative Error"}, results);

    return 0;
}
