
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        nums.sort()
        res = []


        for elm in nums:
            if elm not in d:
                d[elm] = 1
            else:
                d[elm] += 1

        for i in range(k):
            key = max(d, key=d.get)
            value = d.pop(key)
            res.append(key)
            
            
        return res
       