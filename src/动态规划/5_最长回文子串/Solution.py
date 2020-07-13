# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

class Solution(object):
    def expandC(self, s, left, right):
        while left>0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        fi_l = 0
        fi_r = 0
        for i in range(len(s)):
            l1,r1 = self.expandC(s,i,i)
            l2,r2 = self.expandC(s,i,i+1)
            if r1-l1 > fi_r-fi_l:
                fi_l, fi_r = l1, r1
            if r2-l2 > fi_r-fi_l:
                fi_l, fi_r = l2, r2
        return s[fi_l:fi_r+1]
