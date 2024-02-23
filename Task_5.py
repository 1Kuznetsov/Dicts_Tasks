def main():
    N = int(input())
    tree = {}

    for i in range(N):
        parent, progeny = input().split()

        if parent not in tree:
            tree[parent] = [progeny]
        else:
            tree[parent].append(progeny)

    name = input()

    while name not in tree:
        name = input()

    print(progeny_count(tree, name))


def progeny_count(graph, node):
    cnt = 0
    if node in graph:
        for child in graph[node]:
            cnt += 1 + progeny_count(graph, child)

    return cnt


if __name__ == '__main__':
    main()
