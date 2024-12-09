class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        else:
            for i in range(n):
                if pow(2,i)==n:
                    return True
            return False