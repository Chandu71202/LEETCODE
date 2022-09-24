class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        if(k>0):
            res = []
            for i in range(len(code)):
                if(i+1+k<=len(code)):
                    s = sum(code[i+1:i+1+k])
                    res.append(s)
                else:
                    a = i+1+k - len(code)
                    print(code[i+1:i+1+a+1])
                    s = sum(code[i+1:])+sum(code[:a])
                    res.append(s)
            return res
        else:
            res = []
            for i in range(len(code)):
                if(i+k<0):
                    s = sum(code[k+i:]) + sum(code[:i])
                    res.append(s)
                else:
                    s = sum(code[i+k:i])
                    res.append(s)
            return res
                
