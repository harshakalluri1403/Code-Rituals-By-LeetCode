#Merge Sort
#time complexity N log N #Efficient sort
arr=[1,2,54,2,9,1,89,90]
def merge(left,right):
    merged=[]
    i=0
    j=0
    while i<len(left) and j<len(right):

        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
        
            merged.append(right[j])
            j+=1
    merged +=left[i:]+right[j:]
    return merged
    

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)

print(merge_sort(arr))
