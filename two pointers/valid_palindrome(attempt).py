class Solution:
    def isPalindrome(self, s: str) -> bool:
            test = "".join([x.lower() for x in s if x.isalnum()])
            return test == test[::-1]