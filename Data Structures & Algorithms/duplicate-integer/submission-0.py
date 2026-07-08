class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original = set()
        for i in nums:
            if i in original:
                return True
            original.add(i)
        return False

        
        