##mutable immutable

# intはimmutableになるため参照されるメモリが異なる
num1 = 10
print(id(num1))

num2 = num1

print(id(num2))

num1 += 100
print(id(num1))

print('num1',num1)
print('num2',num2)

#アンパック代入

data = [2,34,4,8]
m,n,*o = data
*a,b,c = data
print(a)

#[]
print(o)
data2 = [1,2]
a2,b2,*c2 = data2
print(c2)

#リストの先頭・末尾のみ
a,*_,b = data
print('a:',a,'b:',b)

#リスト指定（割り当て無し）
a,_,b,_ = data
print('a:',a,'b:',b)

#入れ子
data3 = [2,3,[44,55,66]]
x,y,(x1,y1,z1) = data3
print('x1:',x1)

#メモリの比較と値の比較
data4 = [1,2]
data5 = [1,2]
#値のみ比較:true
print(data4==data5)
#メモリを比較:false
print(data4 is data5)

#比較演算子
x=15
print(9<x<30)

#for は文字列を1文字単位で扱う
for value in "hello world":
  print("value:",value)

#range1~5
for l in range(1,6):
  print("l:",l)

#range+2づつ
for l in range(1,6,2):
  print("l:",l)

#rangeをリスト化
lis = list(range(1,10,3))
print("lis:",lis)

#イテレーターとは
# 連続データ(リスト・集合・タプル)を操作するオブジェクト
# EX) 100GBのデータを読み取るとき1度に全てを読み込むとメモリがパンパン
#     →1行ずつ読み込んで、読み込んだデータをその都度破棄する

#リスト内包
data = [3,4,5,6]
data2 = [i * 2 for i in data]
print('data:',data)

data = [3,4,5,6]
data2 = [i * 2 for i in data if i > 4]
print('data2:',data2)



#九九
for i in range(1,10):
  for j in range(1,10):
    print(i*j,end=" ")
  print()

