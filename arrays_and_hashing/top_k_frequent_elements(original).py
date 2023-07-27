class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        # Make dictionary with the num as key and the count of the num as val
        for n in nums:
            if n not in nums_count:
                nums_count[n] = 1
            else:
                nums_count[n] += 1
        

        # Return the k amount of highest occuring nums
        answer = []
        key_list = list(nums_count.keys())
        val_list = list(nums_count.values())
        for x in range(k):
            max_num = max(val_list)
            max_num_index = val_list.index(max_num)
            answer.append(key_list[max_num_index])
            del val_list[max_num_index]
            del key_list[max_num_index]

        return answer