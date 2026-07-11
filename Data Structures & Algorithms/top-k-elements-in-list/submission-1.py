class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # logic - i am thinking of j doing a hash map for each num, ordering hash map, and rhen j returning the top k keys w highest values)
        # ok after watching neetcode, i understand the logic and am going
        # to try to code it (by not looking at answer)
        
        # step 1- hashmap :)
        count = {}
        # step 2 - bucket sort :( scared)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # key bucket sort concept - think abt it 
        # bucket sort is basically opp. of hashmap
        # instead of having the number as the item, the frequency is item
        # and the keys/items or wtv like corresponds to the items, thats the actual number
        # and muliple numners can have same freq so it will all equate 
        for i, v in count.items():
            freq[v].append(i)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

