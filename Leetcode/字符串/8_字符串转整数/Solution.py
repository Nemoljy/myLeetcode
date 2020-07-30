class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        INT_MAX = pow(2,31)-1
        INT_MIN = pow(-2,31)
        str = str.lstrip()   ## 不过似乎不用lstrip()，在正则里直接用' *?[\+-]?\d+'速度更快
        num = int(re.match('[\+-]?\d+',str).group()) if re.match(' *?[\+-]?\d+',str) else 0
        return min(max(INT_MIN,num),INT_MAX)
