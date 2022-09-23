def main():
    [s,t] = [input() for _ in range(2)]
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()
