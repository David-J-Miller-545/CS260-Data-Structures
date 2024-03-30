from numpy import inf
import sys

def floyd(graph):
    n = len(graph)
    pred = []
    dist = []
    for i in range(0, n):
        pred.append([None] * n)
        dist.append([inf] * n)
        for j in range(0, n):
            if graph[i][j] > inf:
                pred[i][j] = j
            dist[i][j] = graph[i][j]
            if j == i:
                pred[i][j] = i
                dist[i][j] = 0
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if (dist[i][k] + dist[k][j]) < dist[i][j]:
                    pred[i][j] = k
                    dist[i][j] = dist[i][k] + dist[k][j]
    return (pred, dist)

def printMatrix(m):
    print("  | ", end="")
    for i in range(0, len(m)):
        print(f"{i:^5} | ", end="")
    print()
    print("--|", end="")
    for i in range(0, len(m)):
        print("-" * 7, end="")
        print("|", end="")
    print()
    for i in range(0, len(m)):
        print(str(i) + " | ", end="")
        for j in range(0, len(m)):
            print(f"{str(m[i][j]):^5}" + " | ", end="")
        print()

def inputGraph():
    g = []
    for line in sys.stdin:
        g.append(line.replace('\n', ''))
    for i in range(0, len(g)):
        temp = g[i].split()
        g[i] = [inf] * len(g)
        for j in range(1, len(temp)):
            g[i][int(temp[j].split(",")[0])] = int(temp[j].split(",")[1])
    for i in range(0, len(g)):
        for j in range(0, len(g)):
            if g[i][j] < inf:
                g[j][i] = g[i][j]
    return g

def main():
    g = inputGraph()
    print("\nAdj. Matrix:")
    printMatrix(g)
    floydResult = floyd(g)
    print("\nPred:")
    printMatrix(floydResult[0])
    print("\nDist:")
    printMatrix(floydResult[1])

if __name__ == "__main__":
    main()