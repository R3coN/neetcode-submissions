class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for s in strs:
            a = a + str(len(s)) + "#" + s
        return a
    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        decoded_s = []
        while i < n:
            j = i
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded_s.append(s[i : i + length])
            i = i + length
        return decoded_s
