class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        dec = []
        while len(s) > 0:
            index = s.find("#")
            stlen = int(s[:index])
            word = s[index+1:index+1+stlen]
            dec.append(word)
            s = s[index+1+stlen:]
        return dec
        
