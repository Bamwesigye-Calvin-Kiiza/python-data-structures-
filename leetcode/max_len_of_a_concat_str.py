# class Solution(object):
#     def maxLength(self, arr):
        
#         def is_unique(s):
#             return len(set(s)) == len(s)

#         def backtrack (start,current,max_length):

#             if is_unique(current):
#                 max_length = max(max_length,len(current))
            
#             for i in range(start,len(arr)):
#                 new_str = current + arr[i]

#                 max_length = backtrack(i + 1, new_str, max_length)
                
#             return max_length 
#         return backtrack(0,'',0)

class Solution(object):
    def maxLength(self,arr):
        
        def is_unique(st):
            return len(st) == len(set(st))
        
        def check(start,current, max_length):
            if is_unique(current):
                max_length = max(len(current), max_length)
            
            for i in range(start, len(arr)):
                new_str  = current + arr[i]
                
                max_length = check(i+1,new_str,max_length)
                
            return max_length
        return check(0,'',0)
            
        
solution = Solution()
arr1 = ["un", "iq", "ue"]
arr2 = ["cha", "r", "act", "ers"]
arr3 = ["abcdefghijklmnopqrstuvwxyz"]

print(solution.maxLength(arr1))  # Output: 4
print(solution.maxLength(arr2))  # Output: 6
print(solution.maxLength(arr3))  # Output: 26