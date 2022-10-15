class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        for i in mat:
            ans.append(i.count(1))
        final_ans=[]
        while(k):
            z=ans.index(min(ans))
            final_ans.append(z)
            ans[z]=max(ans)+1
            k-=1
        return final_ans
