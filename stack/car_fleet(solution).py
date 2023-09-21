class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # list comprehension :)
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p,s in sorted(pair)[::-1]: # Reverse sorted order
            # Want to know what time it will take for car to get to destination
            stack.append((target - p) / s)
            # Does this overlap with top of stack?
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)