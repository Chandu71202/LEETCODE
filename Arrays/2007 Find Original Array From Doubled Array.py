class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        q = []
        l = []
        changed.sort()
        for i in range(len(changed)):
            h = changed[i] /2
            if q and h == q[0]:
                l.append(q.pop(0))
            else:
                q.append(changed[i])
        return l if len(q) == 0 else []
