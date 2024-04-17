#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

// Analogous to the linspace function in Python
std::vector<double> linspace(double start, double end, int n)
{
    std::vector<double> vec(n);
    const double increment = (end - start) / (n - 1);
    for (int i = 0; i < n; ++i)
        vec[i] = start + double(i) * increment;
    return vec;
}

// Print a vector to the standard output
template <typename T>
void print(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
        std::cout << elem << " "; // Print each element
    std::cout << std::endl;       // Print a newline
}

// Print a vector to a file
template <typename T>
void save(const std::vector<T> &vec, const std::string &filename,
          const std::string &header = "")
{
    std::ofstream file(filename); // Open the file
    if (file.is_open())
    { // Check for successful opening
        if (!header.empty())
            file << "# " << header << std::endl; // Write the header
        for (const auto &elem : vec)
            file << elem << " "; // Write each element
        file << std::endl;       // Write a newline
        file.close();            // Close the file
    }
    else
    {
        std::cerr << "Unable to open file " << filename << std::endl;
    }
}


template <typename T1, typename T2>
void save_to_csv(const std::string &filename, const std::vector<std::pair<T1, T2>> &data, const std::string &header = "r,x")
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    // Write the header if provided
    if (!header.empty())
    {
        file << header << "\n";
    }

    // Write each pair in the vector to the file
    for (const auto &[first, second] : data)
    {
        file << first << "," << second << "\n";
    }

    file.close();
}

#endif // UTILS_H
