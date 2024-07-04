## Question Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters. 

import re

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        else:
            strs=sorted(strs)
            common=""
            substring={}
            for a in strs[0]:
                common+=a
                for c in strs[1:]:
                    if re.search(r"^"+common,c):
                        substring[c]=common
                    else:
                        break
        for i in strs[1:]:
            if i not in substring.keys():
                substring[i]=""
        try:
            return min([a for a in substring.values()])
        except:
            return ""
        

strs = ["flower","flow","flight"]

a = Solution()
b=a.longestCommonPrefix(strs)
print(b)