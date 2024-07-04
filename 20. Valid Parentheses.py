## Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
 
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        print(s)
        for i,j in enumerate(s):
            l=len(stack)
            if j in "([{":
                stack.append(j)
            elif l!=0 and j == ")" and stack[-1] == "(":
                stack.pop()
            elif l!=0 and j == "]" and stack[-1] == "[":
                stack.pop()                
            elif l!=0 and j == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        elif len(stack)%2!=0:
            return False
        else:
            for i,j in enumerate(stack[:int(len(stack)/2)]):
                if j == "(" and stack[int(len(stack)/2):][i]==")":
                    continue
                if j == "[" and stack[int(len(stack)/2):][i]=="]":
                    continue
                if j == "{" and stack[int(len(stack)/2):][i]=="}":
                    continue
                else:
                    return False
            return True


