class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [i for i in range(26)]
        
        def find(n):
            if parent[n]==n:
                return n
            parent[n]=find(parent[n])
            return parent[n]
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            parent[p1]=p2
        
        for a,b,c,d in equations:
            n1 = ord(a)-ord('a')
            n2 = ord(d)-ord('a')
            if b=="=":
                union(n1,n2)
        
        for a,b,c,d in equations:
            n1 = ord(a)-ord('a')
            n2 = ord(d)-ord('a')
            if b=="!":
                p1=find(n1)
                p2=find(n2)
                if p1==p2:
                    return False
        return True
