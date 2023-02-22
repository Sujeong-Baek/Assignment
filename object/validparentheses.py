pairs = {")": "(", "}":"{", "]":"["}

class Solution:
    def isValid(self, s: str):
        stack=[]
        for letter in s:
            if letter in "([{":
                stack.append(letter)
            if not stack:
                return False
            if stack[-1] != pairs[letter]:
                    return False
            stack.pop()
        return not stack
# {)

# stack.top()