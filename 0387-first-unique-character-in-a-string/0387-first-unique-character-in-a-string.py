class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            isunique=True
            for j in range(n):
                if i!=j and s[i]==s[j]:
                    isunique=False
                    break
            if isunique:
                return i
        return -1