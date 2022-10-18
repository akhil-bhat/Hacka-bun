def minmax(a:list,n):
    min= a[0]
    max= a[0]
    if(n==2):
         if(a[0]>a[1]):
             max=a[0]
             min=a[1]
         else:
            max=a[1]
            min=a[0]
    for i in range(2,n):
        if(a[i]>max):
            max=a[i]
        elif(min>a[i]):
            min=a[i]
    return print("Minimum:",min,"Maximum:",max)

A=[54,68,12,86,415,723,721,46,268,267,846,56565]
minmax(A,len(A))


        
        
