class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originals = set()
        for i in nums:
            if i in originals:
                return True
            else:
                originals.add(i)
        return False
        