class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        mx = pref[0]
        for i in range(1,len(pref)):
            a = pref[i]^mx 
            ans.append(a)
            mx = mx^a
        return ans
