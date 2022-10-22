class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        print(tCounter)
        window = Counter() 
        ans = "" 
        last = 0 
        for i,char in enumerate(s):
            window[char] = window.get(char,0)+1
            while window >= tCounter:
                if ans == "" or i - last < len(ans): 
                    ans = s[last:i+1]
                window[s[last]] -= 1 
                last += 1 
        return ans 
