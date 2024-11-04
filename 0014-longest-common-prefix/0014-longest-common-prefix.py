class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]

        # Iterate over the rest of the strings
        for i in range(1, len(strs)):
            # Compare the prefix with the current string
            while not strs[i].startswith(prefix):
                # Reduce the prefix until it matches the start of the string
                prefix = prefix[:-1]
                # If the prefix becomes empty, return immediately
                if not prefix:
                    return ""

        return prefix