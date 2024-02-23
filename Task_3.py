def main():
    N = int(input())
    d = {}

    for i in range(N):
        word, antonym = input().split()
        d[word] = antonym

    ptr = input()

    if ptr in d:
        print(d[ptr])
    elif ptr in d.values():
        for k, v in d.items():
            if v == ptr:
                print(k)
    else:
        print(ptr)


if __name__ == '__main__':
    main()
