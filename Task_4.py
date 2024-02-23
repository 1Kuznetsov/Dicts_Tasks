def main():
    N = int(input())
    d = {}

    for i in range(N):
        ptr = input().split()
        d[ptr[0]] = ptr[1:]

    item = input()

    for k, v in d.items():
        if item in v:
            print(k)


if __name__ == '__main__':
    main()
