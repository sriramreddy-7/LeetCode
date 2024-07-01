class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        r = s.split(" ")
        nums = []
        for i in r:
            if i.isnumeric():
                nums.append(int(i))
        ic = False
        dc = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                ic = True
            elif nums[i] > nums[i + 1]:
                dc = True
            if dc:
                return False
            if nums[i] == nums[i + 1]:
                return False
        else:
            return True