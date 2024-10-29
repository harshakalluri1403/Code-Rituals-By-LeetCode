l=int(input("Length of the array"))
n=[]
for i in range(l):
    element=int(input("Enter the elements:"))
    n.append(element)
x=int(input("Enter the element to search in the array: "))

def linear(n,x,l):
    for i in range(0,l):
        if n[i]==x:
            return i
    return -1

result=linear(n,x,l)
if result==-1:
    print("It is not in the given array")
else:
    print(f"It is given in the array at position: {result+1} ")