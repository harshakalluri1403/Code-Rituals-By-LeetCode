class Solution(object):
    def plusOne(self, digits):
        result = int(''.join(map(str, digits)))
        result += 1
        return [int(x) for x in str(result)]
