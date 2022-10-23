class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if len(set(event1+event2)) < 4:
            return True
        s1 = []
        s2 = []
        for i in event1:
            s1.append(int(i[:2])*60+int(i[3:]))
        for i in event2:
            s2.append(int(i[:2])*60+int(i[3:]))
        c1 = False
        c2 = False
        for i in s2:
            if s1[0]<i<s1[1]:
                c1 = True
        for i in s1:
            if s2[0]<i<s2[1]:
                c2 = True
        return c1 or c2
        
