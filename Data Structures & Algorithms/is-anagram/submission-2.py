class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_ascii_s = {}
        for i in s:
            if i in dict_ascii_s.keys():
                dict_ascii_s[i] = dict_ascii_s[i] + 1
            else:
                dict_ascii_s[i] = 1
        for i in t:
            if i not in dict_ascii_s.keys():
                return False
            else:
                if dict_ascii_s[i] == 0:
                    return False
                dict_ascii_s[i] = dict_ascii_s[i] - 1
        if sum(dict_ascii_s.values()) > 0:
            return False
        return True