from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = sorted(str(n)) 
        for i in permutations(s):
            if int("".join(i)) >= 2**31:
                return -1
            if int("".join(i)) > n:
                return int("".join(i)) 
        return -1
