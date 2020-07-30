class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        maxLen = 0
        sl = list(s)
        
        while r<len(s):
            if sl[r] in sl[l:r]:
                print('...')
                l += 1
            else:
                r += 1
            maxLen = max(maxLen,r-l)
            
        return maxLen