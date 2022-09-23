def main ():
    # 逆パターン
    # a,b = list(map(int,input().split()))
    # c,d = list(map(int,input().split()))
    # s = [input() for _ in range(10)]
    # print (s,'s')
    # s = []
    # for _ in range(10):
    #     s.append(input())
    # print (s,'s')
    ss = [str(input()) for _ in range(10)]
    idx_list = []
    for s in ss:
        pos = []
        for i,a in enumerate(s):
            if a == '#':
                pos.append(i)
            # print('pos',pos)
        idx_list.append(pos)
        # print(idx_list,'index_list')
    a,b = 0,0
    for i, item in enumerate(idx_list):
        if item !=[]:
            a= i+ 1
            break
    for j, item in enumerate(idx_list[::-1]):
        print('item',item)
        if item != []:
            b=10 -j 
            break



if __name__ == "__main__":
    main()



    # N = int(input())
    # a = list(map(int,input().split()))
