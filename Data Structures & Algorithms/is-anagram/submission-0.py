class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= dict()
        d2 = dict()
        chars_s = list(s)
        chars_t = list(t)

        for char in chars_s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1

        for char in chars_t:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1

        return d1 == d2
        