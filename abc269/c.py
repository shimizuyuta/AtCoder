from itertools import combinations
def main():
    n = int(input())
    str_bin_n = bin(n)
    places = []
    ans = []

    for i, a in enumerate(str_bin_n[::-1][:-2]):
        if a=='1':
            places.append(i)
    print('places',places)

    for i in range(len(places)+1):
        for mini_places in combinations(places,i):
            num = 0
            for place in mini_places:
                num += 2 ** place
            ans.append(num)

    ans.sort()
    for a in ans:
        print(a)






if __name__ == "__main__":
    main()