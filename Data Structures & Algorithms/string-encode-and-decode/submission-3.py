class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for s in strs:
            encode_str+=f"{len(s)}#{s}"
        return encode_str

    def decode(self, s: str) -> List[str]:

        res=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
            lenght = int(s[i:j])
            i=j+1
            res.append(s[i:i+lenght])
            i+= lenght
        return res