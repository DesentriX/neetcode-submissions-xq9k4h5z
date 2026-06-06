class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydic = dict()
        res = 0
        l = 0
        
    

        for r in  range(len(s)):
            if s[r] not in mydic:
                mydic[s[r]] = 1
            else:
                mydic[s[r]] +=1

            max_frequency = max(mydic.values())


            while (r - l + 1) - max_frequency > k:
                mydic[s[l]] -=1
                l += 1


            res = max(res, r - l +1)

        return res
            


        