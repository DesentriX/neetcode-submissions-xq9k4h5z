class Solution:
    def hammingWeight(self, n: int) -> int:
        dic = dict()
        s = bin(n)[2:]

        for elm in s:
            if elm not in dic:
                dic[elm] = 1
            else:
                dic[elm] += 1

        return(s.count("1"))

        





       
        