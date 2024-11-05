class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        a=len(words[-1])
        return a