from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        res = defaultdict(list)
        for key,value in d.items():
            res[value].append(key)
        res = sorted(res.items(),reverse=True)
        ans = []
        for i in range(len(res)):
            res[i][1].sort()
            if len(ans)<=k:
                for j in res[i][1]:
                    ans.append(j)
            else:
                break
        return ans[:k]
        
