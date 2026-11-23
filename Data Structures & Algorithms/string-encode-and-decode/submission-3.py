class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        dec = []
        i=0
        while len(s)>i:
            j=i
            while s[j]!='#':
                j+=1
            leng = int(s[i:j])
            dec.append(s[j+1:j+1+leng])
            i=j+1+leng
        return dec

