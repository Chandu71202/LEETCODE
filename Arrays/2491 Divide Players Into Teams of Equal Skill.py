class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0]+skill[-1]
        prod = skill[0]*skill[-1]
        for i in range(1,n//2):
            if skill[i]+skill[n-i-1]!=target:
                return -1
            else:
                prod+=skill[i]*skill[n-i-1]
        return prod
