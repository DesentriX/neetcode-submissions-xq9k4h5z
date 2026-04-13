class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = []
        used = set()
        for i in range(len(strs)):
            if i in used:
                continue
                
            temp = [strs[i]]
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    temp.append(strs[j])
                    used.add(j)
            new.append(temp)
        return new
                

       
        