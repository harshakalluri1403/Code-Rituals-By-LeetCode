class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr=sorted(s)
        t_arr=sorted(t)
        return(s_arr==t_arr)