Maxx = 100005
Graph = [[] for _ in range(Maxx)]


def minSumDigits(N):
    for i in range(1, N + 1):
        From = (i) % N
        To = (i + 1) % N
        Wt = 1
        Graph[From].append([To, Wt])

    for i in range(1, N + 1):
        From = (i) % N
        To = (10 * i) % N
        Wt = 0
        Graph[From].append([To, Wt])

    PQ = []
    Distance = [1e9 for _ in range(N + 2)]

    PQ.append([0, 1])
    src = 1
    Distance[src] = 0
    while (len(PQ) != 0):
        current = PQ.pop(0)[1]
        for neighbours in Graph[current]:
            v = neighbours[0]
            weight = neighbours[1]
            if (Distance[v] > Distance[current] + weight):
                Distance[v] = Distance[current] + weight
                PQ.append([Distance[v], v])

    print((1 + Distance[0]))


N = int(input())
minSumDigits(N)