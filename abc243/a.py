def main():
  V,A,B,C = map(int,input().split())
  # users = [A,B,C]
  # name = ["T","F","M"]
  # i=0

  # while V >=0:
  #   V=V-users[i%3]
  #   i+=1

  # print(name[i%3])

  while True:
    V -= A
    if V<0:
      print("F")
      break 
    V -=B 
    if V<0:
      print("M")
      break
    V -=C
    if V<0:
      print("T")
      break





if __name__ == "__main__":
  main()