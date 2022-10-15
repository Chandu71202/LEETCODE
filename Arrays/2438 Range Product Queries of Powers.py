class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        v = []
        ans1 = []
        while (n > 0):
            v.append(int(n % 2))
            n = int(n / 2)
        for i in range(0, len(v)):
            if (v[i] == 1):
                ans1.append(2**i)
                
        ans = []
        for i,j in queries:
            val = 1 
            for x in range(i,j+1):
                val*=ans1[x]
            ans.append(val%MOD)
        return ans
