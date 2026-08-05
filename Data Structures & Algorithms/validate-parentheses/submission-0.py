class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            "(": ")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for char in s:
            # if chars in matching, that means it has to be one of the keys and the keys r all openings so u can immediately append it tostack
            if char in matching: 
                stack.append(char)
            # if its not in matching if its not a key that means it has to be a closing or a random char either way u can now test to see if it matches the correct corresponding opening or if stack is even like non zero ya know
            else:
                if stack and char == matching[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        else:
            return False  