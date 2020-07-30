class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num_list = [dic[k] for k in s]
        num_list.reverse()
        result = num_list[0]
        for i in range(len(num_list)-1):
            result += num_list[i+1] if num_list[i+1]>=num_list[i] else  -num_list[i+1]
            
        return result
