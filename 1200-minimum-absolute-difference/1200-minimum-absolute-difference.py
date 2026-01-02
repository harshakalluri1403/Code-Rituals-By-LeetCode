class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum=math.inf
        new=[]
        for i in range(len(arr)-1):
            minimum=min(minimum,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minimum:
                new.append([arr[i],arr[i+1]])
        return new

            