class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in dict_s.keys():
                dict_s[sorted_s].append(s)
            else:
                dict_s[sorted_s] = [s]
        a = []
        for i in dict_s.values():
            a.append(i)
        return a