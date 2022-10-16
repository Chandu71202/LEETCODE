from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        word2_dict  = [Counter(i) for i in words2]
        temp = word2_dict[0]
        
        for d in word2_dict:
            for key,value in d.items():
                temp[key] = max(temp.get(key,0), value)
        
        for a in words1:
            c = Counter(a)
            for key,value in temp.items():
                if c.get(key,0)<value:
                    break
            else:
                res.append(a)
        return res
