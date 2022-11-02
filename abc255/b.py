import math 
n,k = map(int,input().split())
ak = list(map(int,input().split()))

xy = [ list(map(int,input().split())) for i in range(n)]
# print(n,k,ak,xy)

light_list = []


for i in ak:
    light_list.append(xy[i-1])


others = [i for i in xy if i not in light_list]

ans_list = []
ans = 0

for i in others:
    for j in light_list:
        aa = math.sqrt(pow(i[0]-j[0],2) + pow(i[1]-j[1],2))
        ans_list.append(aa)

    if min(ans_list) > ans :
        ans = min(ans_list)
    ans_list= []

    
print(ans)
        
        


# black_list = ak - light_list
# print(black_list)