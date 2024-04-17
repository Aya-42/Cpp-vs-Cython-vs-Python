#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>
#include <numeric>
#include "utils.h"

std::vector<double> lorentzian_transform(const std::vector<double> &u, double gamma = 1.0)
{
    std::vector<double> transformed(u.size());
    std::transform(u.begin(), u.end(), transformed.begin(), [gamma](double val)
                   { return gamma / tan(M_PI * (val - 0.5)); });
    return transformed;
}

int main()
{
    // const int n = 100000000; // Number of samples
    const int n = 3; // Number of samples
    std::vector<double> random_uniform(n);

    // Generate random numbers using <random> and std::generate
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    std::generate(random_uniform.begin(), random_uniform.end(), [&]()
                  { return dis(gen); });

    // Lorentzian transform using std::transform
    auto start = std::chrono::high_resolution_clock::now();
    auto transformed_samples = lorentzian_transform(random_uniform);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "C++ Time Taken: " << elapsed.count() << "s\n";

    // Create a histogram of the sampled values using std::for_each and lambda
    std::vector<int> counts(1000, 0);
    double bin_size = 20.0 / 1000;
    std::for_each(transformed_samples.begin(), transformed_samples.end(), [&](double value)
                  {
        int bin = (value + 10) / bin_size;
        if (bin >= 0 && bin < 1000) {
            counts[bin]++;
        } });

    // Prepare data for CSV using transform (to convert bin number and count to a suitable format)
    std::vector<std::vector<double>> histogram_data;
    for (size_t idx = 0; idx < counts.size(); ++idx)
    {
        double bin_edge = -10 + idx * bin_size;
        int count = counts[idx];
        histogram_data.push_back(std::vector<double>{bin_edge, static_cast<double>(count)});
    }

    // Save histogram data to CSV
    save_to_csv("histogram_data_c.csv", {"bin_edge", "count"}, histogram_data);

    return 0;
}
