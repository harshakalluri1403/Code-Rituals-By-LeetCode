class Solution(object):
    def plusOne(self, digits):
        # Convert the list of digits to a single integer
        result = int(''.join(map(str, digits)))
        # Increment the number by 1
        result += 1
        # Convert the incremented number back to a list of digits
        return [int(x) for x in str(result)]
