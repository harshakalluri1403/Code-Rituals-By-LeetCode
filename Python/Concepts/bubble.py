n=int(input("Enter the length of the array"))
array=[]
for i in range(n):
    element=int(input())
    array.append(element)
    
    
def sort(array):
    for i in range(n-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
sort(array)
print(array)