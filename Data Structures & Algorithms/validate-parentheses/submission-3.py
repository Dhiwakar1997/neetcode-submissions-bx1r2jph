class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n==0 or n%2==1:
            return False

        stack = []

        brackets={")":"(","}":"{","]":"["}

        for val in s:
            if val in brackets:
                if stack:
                    match= stack.pop()
                else:
                    return False
                if match!=brackets.get(val,""):
                    return False
            else:
                stack.append(val)
        if stack:
            return False
        return True