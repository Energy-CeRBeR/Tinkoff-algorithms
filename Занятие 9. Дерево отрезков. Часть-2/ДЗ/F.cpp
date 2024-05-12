#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <cassert>


struct Center {
	long long x;
	long long y;
	long long id;
};


int main() {
	int n;
	scanf("%*d %*d %d", &n);

	std::vector<Center> centers(n);
	for (int id = 0; id < n; id++) {
		double x, y;
		scanf("%lf %lf", &x, &y);
		centers[id] = Center{ (long long)(x * 2), (long long)(y * 2), id };
	}

	std::vector<long long> y(n);
	for (int i = 0; i < n; i++) {
		y[i] = centers[i].y;
	}

	std::sort(y.begin(), y.end());
	std::sort(centers.begin(), centers.end(), [](const Center& left, const Center& right) {
		return left.x < right.x;
		});
	y.erase(std::unique(y.begin(), y.end()), y.end());

	std::vector<long long> x(y.size() * 2, 0);
	std::function<long long(int)> getX = [&](int index) {
		long long sum = 0;
		for (; index >= 0; index = (index & (index + 1)) - 1) {
			sum += x[index];
		}
		return sum;
		};

	std::function<void(int, long long) > addSinceX = [&](int index, long long extra) {
		for (; index < (int)x.size(); index = index | (index + 1)) {
			x[index] += extra;
		}
		};

	std::function<void(int, int, long long)> addRangeX = [&](int first, int after, long long extra) {
		addSinceX(first, extra);
		addSinceX(after, -extra);
		};

	std::vector <long long> ans(n, 0);
	for (Center center : centers) {
		auto it = std::lower_bound(y.begin(), y.end(), center.y);
		assert(it != y.end() && *it == center.y);
		int index = int(it - y.begin());
		long long dist = center.x - getX(index);
		assert(dist > 0);
		assert(ans[center.id] == 0);
		ans[center.id] = dist;

		it = std::upper_bound(y.begin(), y.end(), center.y - dist);
		int first = int(it - y.begin());
		it = std::upper_bound(y.begin(), y.end(), center.y + dist);
		int after = int(it - y.begin());
		addRangeX(first, after, dist * 2);
	}

	for (long long value : ans) {
		assert(value != 0);
		printf("%lld\n", value);
	}


	return 0;

}