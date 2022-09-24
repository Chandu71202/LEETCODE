class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l1 = len(nums)
        l = []
        for i in nums:
            l.append(int(i,2))
        l.sort()
        s=max(l)
        print(l)
        for i in range(s):
            if i not in l:
                return (l1-len(bin(i)[2:]))*'0'+bin(i)[2:]
        return (l1-len(bin(l[-1]+1)[2:]))*'0'+bin(l[-1]+1)[2:]
