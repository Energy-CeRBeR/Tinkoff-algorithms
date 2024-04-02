#include <bits/stdc++.h>
using namespace std;

const int Maxx = 100005;
int N;
vector<pair<int, int> > Graph[Maxx];

/// Dijkartas algorithm to find the shortest distance
void Dijkartas(int source)
{
	priority_queue<pair<int, int>, vector<pair<int, int> >,
								greater<pair<int, int> > > PQ;

	// Initialize all distances to be infinity
	vector<int> Distance(N + 2, 1e9);

	// Push source in Priority Queue
	PQ.push(make_pair(0, source));
	int src = source;
	Distance[src] = 0;
	while (!PQ.empty()) {
		int current = PQ.top().second;
		PQ.pop();
		for (auto& neighbours : Graph[current]) {
			int v = neighbours.first;
			int weight = neighbours.second;
			if (Distance[v] > Distance[current] + weight) {
				Distance[v] = Distance[current] + weight;
				PQ.push(make_pair(Distance[v], v));
			}
		}
	}

	cout << 1 + Distance[0] << endl;
	return;
}

// Function to calculate the minimum possible sum of digits
void minSumDigits(int N)
{
	// Build a graph of N vertices with edge weight 1
	for (int i = 1; i <= N; ++i) {
		int From = (i) % N;
		int To = (i + 1) % N;
		int Wt = 1;
		Graph[From].push_back(make_pair(To, Wt));
	}

	// In the same graph add weights 0 to 10's multiple of node X
	for (int i = 1; i <= N; ++i) {
		int From = (i) % N;
		int To = (10 * i) % N;
		int Wt = 0;
		Graph[From].push_back(make_pair(To, Wt));
	}

	// Run dijkartas to find the shortest distance from 1 to 0
	Dijkartas(1);
	return;
}

// Driver Code
int main()
{
    cin >> N;

	minSumDigits(N);

	return 0;
}
