rows=int(input('no of  rows: '))
col=int(input('no of  cols: '))

for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1:
            print('+',end='')
        else:
            if j==0 or j==col-1 or j==i:
                print('+',end='')
            else:
                print(' ',end='')               
    print()