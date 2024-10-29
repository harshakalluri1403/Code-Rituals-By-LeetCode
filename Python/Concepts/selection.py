array=[5,34,12,1,45]
n=len(array)
def sort(array):
    for i in range(n-1):
        minpos=i
        for j in range(i,n):
            if array[j]<array[minpos]:
                minpos=j
        array[i],array[minpos]=array[minpos],array[i]
        
sort(array)
print(array)