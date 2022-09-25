from itertools import combinations


n,m = map(int,input().split())

n_list = list(range(1,m))
ans = list(combinations(range(1,m+1),n))

for i in range(len(ans)):
  for j in range(n):
    print(ans[i][j],end='')
  print()

