class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            frm = j + 1
            to = frm + length
            # tips: start is inclusive, end is exclusive. e.g. s[0:3], actual: end at index 2.
            res.append(s[frm:to])
            i = to 
            
        return res

