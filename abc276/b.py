# これだとAC×2,WA×1,TLE×7(WAはテストケースが発表され次第確認)

# n,m = list(map(int,input().split()))
# list_m = []
# for i in range(m):
#     list_m.append([int(i) for i in input().split()])
# ans = []

# for i in range(1,m+1):
#     for j in list_m:
#         if i in j:
#             for k in j:
#                 if k != i:
#                     ans.append(k)
#     if i > n:
#         break
#     if len(ans) == 0:
#         print(0)
#     else:
#         ans.sort()
#         ans.insert(0,len(ans))
#         for item in ans:
#             print(item, end=" ")
#         print(' ')
#     ans = []

#隣接リストを使用
    
n,m = map(int,input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    a[u-1].append(v)
    a[v-1].append(u)

for (i,v) in enumerate(a):
    v.sort()
    print(len(v),*v)

