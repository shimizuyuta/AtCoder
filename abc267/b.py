def main():
    n = [int(i) for i in input()]
    if(n[0]==1):print('No')

    column = list(range(7))
    column[0] = n[6]
    column[1] = n[3]
    column[2] = 1 if (n[1] and n[7]) ==1 else 0
    column[3] = n[4]
    column[4] = 1 if (n[2] and n[8]) == 1 else 0
    column[5] = n[5]
    column[6] = n[9]
    print(search(column))

def search(column):
    for i in range(7):
        for j in range(i):
            if column[i] and column[j]:
                for k in range(j+1,i):
                    if not column[k]:
                        return 'Yes' 
    return 'No'



if __name__ == "__main__":
    main()