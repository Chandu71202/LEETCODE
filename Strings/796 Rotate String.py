class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s,goal=map(list,[s,goal])
        for i in range(len(s)):
            s.append(s.pop(0))
            if(s==goal):
                return True
        return False
