n = 5		
for row in range(0,n+1):
    for col in range(0,n):
        if(row==0 and col%2!=0 ) or (row==1 and col%2==0) or (row==2 and (col==0 or 4)) or (row-col==3) or (row+col==7):
            print('o',end='')
        else:
            print(' ',end='')
              
    print()
