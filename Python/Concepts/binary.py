l=int(input("Enter the length of the array"))
n=[]
for i in range(l):
    element=int(input("Enter the elements:"))
    n.append(element)
x=int(input("Enter the search element: "))
low=0
high=l-1

def binary(n,x,low,high):
    if high>=low:
        mid=(low+high)//2
        if n[mid]==x:
            return mid
        elif n[mid]>x:
            return binary(n,x,low,mid-1)
        else:
            return binary(n,x,mid+1,high)
        
    return -1
        
result=binary(n,x,low,high)

if result==-1:
    print("element not found")
else:
    print("Element found at index",result)