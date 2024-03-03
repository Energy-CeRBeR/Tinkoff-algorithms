#include <iostream>
#include <deque>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>


int findIndex(std::deque<int>& dq, int x) {
    int l, r;
    l = 0;
    r = dq.size() - 1;
    while (l <= r) {
        if (dq[l] == x) {
            return l;
        }
        if (dq[r] == x) {
            return r;
        }
        l++;
        r--;
    }
}


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

	int n;
	std::cin >> n;
    std::string input;
    std::getline(std::cin, input);

	std::deque<int> queue;
    for (int i = 0; i < n; i++) {
        std::string input;
        std::getline(std::cin, input);
        std::istringstream stream(input);
        int num1, num2;
        if (stream >> num1) {
            if (stream >> num2) {
                if (num1 == 1) { queue.push_back(num2); }
                else {
                    int index = findIndex(queue, num2);
                    std::cout << index << "\n";
                }
            }
            else {
                if (num1 == 2) {queue.pop_front();}
                else if (num1 == 3) {queue.pop_back();}
                else { std::cout << queue[0] << "\n"; }
            }
        }
    }

	return 0;
}