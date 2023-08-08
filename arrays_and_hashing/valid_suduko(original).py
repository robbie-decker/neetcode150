class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        checked_rows = [[],[],[],[],[],[],[],[],[]]
        checked_cols = [[],[],[],[],[],[],[],[],[]]
        checked_boxes = [[],[],[],[],[],[],[],[],[]]
        addition_factor = 0

        for x, row in enumerate(board):
            # Very important step so that our box index goes from 0-8 instead of 0-4
            if (x) % 3 == 0 and x != 0:
                addition_factor += 3
            for y, col_val in enumerate(row):
                if col_val != ".":
                    # This is the easy part. Check if cols and rows have been repeated
                    if col_val not in checked_rows[x] and col_val not in checked_cols[y]:
                        checked_rows[x].append(col_val)
                        checked_cols[y].append(col_val)
                        
                        # This calculates the box number using floor division
                        box_index = ((x + addition_factor) // 3) + ((y + addition_factor) // 3) 

                        if col_val not in checked_boxes[box_index]:
                            checked_boxes[box_index].append(col_val)
                        else: 
                            return False

                    else:
                        return False

        return True  