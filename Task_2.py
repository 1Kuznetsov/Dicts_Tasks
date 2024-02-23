def main():
    N = int(input())
    d = {}

    for i in range(N):
        ru, eng = input().split()
        d[ru] = eng

    ptr = input().split()

    for j in range(len(ptr)):
        if ptr[j] in d:
            ptr[j] = d[ptr[j]]

    print(' '.join(ptr))


if __name__ == '__main__':
    main()
