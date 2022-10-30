# coding: utf-8
# Your code here!

# inputの内容　2 3 5 1 2 4    1行空白区切り
WARUKAZU = 998244353

def main():
    a,b,c,d,e,f = map(int,input().split())
    abcdef = (a*b*c) - (d*e*f)
    ans = abcdef% WARUKAZU
    print(ans)
    


if __name__ == "__main__":
  main()
  