class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  # Create a dictionary to store numbers and their indices
        
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the required complement
            
            if complement in num_to_index:  # Check if the complement is in the dictionary
                return [num_to_index[complement], index]  # Return the indices of the complement and the current number
            
            num_to_index[num] = index 
        
