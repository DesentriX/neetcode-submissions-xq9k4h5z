class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)

        for elm in strs:
            d[tuple(sorted(elm))].append(elm)

        for v in d.values():
            res.append(v)

        return res

        

        


        
                

       
        