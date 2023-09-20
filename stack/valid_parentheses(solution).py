class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        
        for c in s:
            # Char is a closing parenthesis
            if c in closeToOpen:
                # Stack is not empty and last elem is the corresponding opening parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False