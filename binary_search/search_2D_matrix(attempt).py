class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First binary search if target is between first elem and last elem of current row
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r + l) // 2
            if target < matrix[m][0]:
                r = m - 1
            # Found the right row
            # Then binary search the row to try to find the element
            elif target >= matrix[m][0] and target <= matrix[m][-1]:
                correct_row = matrix[m]
                l2, r2 = 0, len(correct_row) - 1
                while l2 <= r2:
                    m2 = (l2 + r2) // 2
                    if correct_row[m2] == target:
                        return True
                    elif correct_row[m2] < target:
                        l2 = m2 + 1
                    elif correct_row[m2] > target:
                        r2 = m2 - 1
                return False
                
            elif target > matrix[m][0] and target > matrix[m][-1]:
                l = m + 1
        return False