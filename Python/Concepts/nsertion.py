arr=[23,45,1,34,76]

def sort(arr):
    for i in range(1,len(arr)):
        j=i

        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
sort(arr)
print(arr)