def main():
    # Step 1: Parse the input
    N, M = map(int, input().split())
    existing_lines = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    proposals = [tuple(map(int, input().split())) for _ in range(K)]
    P = int(input())
    requirements = [tuple(map(int, input().split())) for _ in range(P)]

    # Step 2: Simulate the network with existing lines
    network = {}
    for u, v, t in existing_lines:
        network.setdefault(u, []).append((v, t))
        network.setdefault(v, []).append((u, t))

    # Step 3: Determine which proposals need to be satisfied
    satisfied_proposals = []
    for proposal_num, (u, v, t, c) in enumerate(proposals, start=1):
        if (u not in network or v not in network or
                all(time > t for _, time in network[u]) or
                all(time > t for _, time in network[v])):
            satisfied_proposals.append((c, proposal_num))

    # Step 4: Output the result
    if not satisfied_proposals:
        print(0)
    else:
        min_cost = min(satisfied_proposals)[0]
        satisfied_proposals = [num for cost, num in satisfied_proposals if cost == min_cost]
        print(len(satisfied_proposals))
        print(*sorted(satisfied_proposals))

if __name__ == "__main__":
    main()