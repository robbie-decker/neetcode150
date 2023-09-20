class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        openParentheses = ["(", "[", "{"]
        closeParentheses = [")", "]", "}"]
        for c in s:
            if c in openParentheses:
                myStack.append(c)
            elif c in closeParentheses:
                if len(myStack) == 0:
                    return False
                previousChar = myStack.pop()
                print(previousChar, c)
                if openParentheses.index(previousChar) != closeParentheses.index(c):
                    return False
        return True if len(myStack) == 0 else False