Maxx = 100005
Graph = [None for _ in range(Maxx)]
for i in range(Maxx):
    Graph[i] = []


def Dijkartas(source):
    PQ = []
    Distance = [1e5 for _ in range(N + 2)]

    PQ.append([0, source])
    src = source
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
    return


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

    Dijkartas(1)
    return


N = int(input())
minSumDigits(N)