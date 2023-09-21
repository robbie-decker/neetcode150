# This was not accepted but I still think this is a really slick answer. 
# Think int rounding was what did me in but overall I am pretty happy with this
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = [] # pair: [position, speed]
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        
        stack.sort()
        while stack:
            closerIndex, closerSpeed = stack.pop()
            # Not on last element
            if stack:
                furtherIndex, furtherSpeed = stack[-1]
                # Cars behind going same speed or less. They will never meet
                if furtherSpeed - closerSpeed <= 0 :
                    fleets += 1
                else:
                    timeDiff = round((closerIndex - furtherIndex) / (furtherSpeed - closerSpeed))
                    # The previous car does not have enough time to catch up. It will be its own fleet
                    if closerIndex + (closerSpeed * timeDiff) > target:
                        fleets += 1
                    # The previous car does catch up so now the fleet is going the further cars speed
                    else:
                        stack.pop()
                        stack.append([closerIndex + (closerSpeed * timeDiff), closerSpeed])

            else:
                fleets += 1
        return fleets
            