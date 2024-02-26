#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>


int main() {
	double a, b, c, d;
	std::cin >> a >> b >> c >> d;
	double p = (3 * a * c - b * b) / (3 * a * a);
	double q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a);
	double Q = (p / 3) * (p / 3) * (p / 3) + (q / 2) * (q / 2);

	assert(Q >= 0);
	if (Q < 0) {
		Q = 0;
	}
	double alpha = std::cbrt(-q / 2 + std::sqrt(Q));
	double beta = std::cbrt(-q / 2 - std::sqrt(Q));
	
	double y = alpha + beta;
	double x = y - b / (3 * a);
	std::cout << x;

	return 0;
}