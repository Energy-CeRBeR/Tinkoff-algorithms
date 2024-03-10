#include <iostream>
#include <vector>

int main() {
	int n, h1, m1, s1, h2, m2, s2, t1, t2;
	std::cin >> n;
	std::vector<int> t(86400);
	int offset = 0;
	for (int i = 0; i < n; i++) {
		std::cin >> h1 >> m1 >> s1 >> h2 >> m2 >> s2;
		t1 = 3600 * h1 + 60 * m1 + s1;
		t2 = 3600 * h2 + 60 * m2 + s2;

		if (t1 < t2) {
			for (int j = t1; j < t2; j++) {
				t[j]++;
			}
		}
		else if (t2 < t1) {
			for (int j = 0; j < t2; j++) {
				t[j]++;
			}
			for (int j = t1; j < 86400; j++) {
				t[j]++;
			}
		}
		else {
			offset++;
			}
	}

	int count = 0;
	for (int j = 0; j < 86400; j++) {
		if (t[j] == n - offset) {
			count++;
		}
	}
	std::cout << count;

	return 0;
}