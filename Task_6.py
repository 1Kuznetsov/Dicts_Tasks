def main():
    N = int(input())
    while N <= 0:
        N = int(input())

    G = read_graph()

    start_city, end_city = input().split()

    while start_city not in G or end_city not in G:
        start_city, end_city = input().split()

    dist = dijkstra(G, start_city)
    print(dist)
    print(dist[end_city])


def read_graph():
    M = int(input())
    while M <= 0:
        M = int(input())

    G = {}

    for i in range(M):
        city_1, city_2, dist = input().split()
        dist = int(dist)
        assert dist > 0
        add_vertex(G, city_1, city_2, dist)
        add_vertex(G, city_2, city_1, dist)

    return G


def add_vertex(graph, a, b, weight):
    if a not in graph:
        graph[a] = {}
    graph[a][b] = weight


def dijkstra(graph, start):
    dist = {}
    queue = []
    dist[start] = 0
    queue.append(start)

    while queue:
        curr = queue.pop(0)

        for v in graph[curr]:
            if v not in dist or dist[curr] + graph[curr][v] < dist[v]:
                dist[v] = dist[curr] + graph[curr][v]
                queue.append(v)

    return dist


if __name__ == '__main__':
    main()
