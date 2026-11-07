class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "$" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            content_length = int(s[i:j])

            content = s[j + 1: j + 1 + content_length]
            result.append(content)
            i = j + 1 + content_length
        return result   

# string