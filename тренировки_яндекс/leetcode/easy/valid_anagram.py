class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        dct = {}

        for let in s:
            if let in dct:
                dct[let] += 1
            else:
                dct[let] = 1

        for let in t:
            if let in dct:
                dct[let] -= 1
                if dct[let] == -1:
                    return False
            else:
                return False

        return True        