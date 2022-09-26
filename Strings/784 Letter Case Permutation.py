class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i in s:
            if i.isdigit():
                ans = [j+i for j in ans]
            else:
                t1 = [j+i.lower() for j in ans]
                t2 = [j+i.upper() for j in ans]
                ans = t1+t2 
        return ans
