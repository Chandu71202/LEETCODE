class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            pass
        elif len(set(chars))==1:
            n = len(chars)
            chars.append(chars[0])
            c = str(n)
            for i in c:
                chars.append(i)
            chars[:n]=[]
        else:
            a = chars[0]
            c = 0
            local = 0
            n = len(chars)
            for i in chars:
                if (local<n):
                    if i==a:
                        c+=1
                    else:
                        chars.append(a)
                        if c!=1:
                            for j in str(c):
                                chars.append(j)
                        c = 1
                        a = i
                else:
                    chars.append(a)
                    if c!=1:
                        for j in str(c):
                            chars.append(j)
                    break
                local+=1 

            chars[:n]=[]
