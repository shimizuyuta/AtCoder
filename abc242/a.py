A,B,C,X = map(int,input().split())
if A >= X:
  print(1)
elif B >= X:
  print(C/(B-A))
else:
  print(0)

