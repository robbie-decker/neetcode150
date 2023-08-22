class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Have position of left and right
        left, right = 0, len(numbers) - 1
        while(left < right):
            mySum = numbers[left] + numbers[right]
            if mySum == target:
                    return [left + 1, right + 1]
            else:
            # If left + right is less than target move left's index 1
                if mySum < target:
                    left += 1
            # If left + right is greater than targer move right over 1
                else:
                    right-=1
    
        