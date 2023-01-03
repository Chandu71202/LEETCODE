class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rearrange = []
        n = len(strs)
        n1 = len(strs[0])
        for i in range(n1):
            a = ""
            for j in range(n):
                a+=strs[j][i]
            rearrange.append(a)
        count = 0
        for i in rearrange:
            if i!=''.join(sorted(i)):
                count+=1
        return count
        
