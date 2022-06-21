def main():
  a,b = map(int,input().split())
  if abs(a-b) == 1 or abs(a-b) == 9:
    ans = "Yes"
  else:
    ans = "No"
  print(ans)
  

if __name__ == "__main__":
    main()