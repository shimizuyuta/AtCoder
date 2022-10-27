# 2 2
# 3 1 4 7
# 2 5 9
# 1 3
# 2 1


n,q = map(int,input().split())
Ln = [list(map(int,input().split())) for _ in range(n)]
st = [list(map(int,input().split())) for _ in range(q)]

for j in range(len(st)):
    a,b  = st[j]
    
    print(Ln[a-1][b])
