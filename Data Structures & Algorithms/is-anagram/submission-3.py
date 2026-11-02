class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
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
            return True
        else:
            return False