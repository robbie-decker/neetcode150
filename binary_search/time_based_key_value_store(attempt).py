# Could not get past the time limit for the life of me.
# Feel like I got pretty close tho. I think I needed a better way to insert
# The new timestamps while keeping the array sorted. Could not find a better way than
# to just using sorted() on the array


# JUST FUCKING KIDDING I GOT IT
# Changing the insert to be in O(n) time and to insert the element in
# a sorted way did the trick

class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        isPresent = self.dict.get(key, -1)
        # Need to make new dict for key
        if isPresent == -1:
            self.dict[key] = [(timestamp, value)]
        else:
            # Want to insert in a sorted way
            # Probably a way to bin search this
            self.dict[key].append((timestamp, value))
            lst = self.dict[key]
            i = len(lst)  - 1
            while i > 0 and lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                i -= 1
            self.dict[key] = lst

    def get(self, key: str, timestamp: int) -> str:
        timeStampDict = self.dict.get(key, -1)
        if timeStampDict == -1:
            return ""
        # This is where we bin search
        else:
            l, r = 0, len(timeStampDict) - 1
            timeStampDict
            prev = timeStampDict[0]
            while l <= r:
                m = (l + r) // 2
                if timeStampDict[m][0] < timestamp:
                    if timeStampDict[m][0] > prev[0]:
                        prev = timeStampDict[m] 
                    l = m + 1
                elif timeStampDict[m][0] > timestamp:
                    r = m - 1
                else:
                    return timeStampDict[m][1]
            if prev[0] > timestamp:
                return ""
            else:
                return prev[1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)