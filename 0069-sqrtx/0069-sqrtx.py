class Solution(object):
    def mySqrt(self, x):
        # Edge cases: 0 and 1
        if x == 0 or x == 1:
            return x
        
        low, high = 0, x
        ans = 0
        
        # Perform binary search
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  # Exact square root found
            elif mid * mid < x:
                low = mid + 1
                ans = mid  # Store the floor of the square root
            else:
                high = mid - 1
        
        return ans
