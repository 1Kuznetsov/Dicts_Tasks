def main():
    ptr = input()

    d = {word: ptr.count(word) for word in ptr.split()}
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)

    print(*dict(sorted_dict).keys(), sep='\n')


if __name__ == '__main__':
    main()
