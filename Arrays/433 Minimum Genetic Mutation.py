class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue, seen = deque([(start, 0)]), {start}      
        while queue:
            s, n = queue.popleft()                      
            if s == end: return n                                                                  
            for i in range(8):                          
                for ch in 'ACGT':                                                                     
                    m = s[:i]+ch+s[i+1:]                                              
                    if m in bank and m not in seen:       
                        seen.add(m)
                        queue.append((m, n+1))
        return -1
