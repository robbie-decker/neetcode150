class Solution:
    def climbStairs(self, n: int) -> int:
        # Okay so recursion does not seem to work. 
        # Seems like answers follow a Fibonacci sequence so imma try that

        def fib(first, second, i) -> int:
            temp = first + second
            i += 1
            if i >= n:
                return temp
            else:
                first = second
                second = temp
                return fib(first, second, i)


        return fib(0,1,0)