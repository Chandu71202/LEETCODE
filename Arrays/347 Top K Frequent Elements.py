class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # approach 1 fails for last input TLE
        # d={}
        # for i in nums:
        #     d[i]=nums.count(i)
        # d = sorted(d.items(), key=lambda kv: kv[1],reverse=True)
        # l=[]
        # for i in d:
        #     l.append(i[0])
        # return l[:k]
        
        #approach 2 passes for all
        
        # c = Counter(nums)
        # c=dict(c)
        # c = sorted(c.items(), key=lambda kv: kv[1],reverse=True)
        # l=[]
        # for i in range(k):
        #     l.append(c[i][0])
        # return l
        
        #approach 3 same but differs in returning
        c = Counter(nums)
        return [i for i,j in c.most_common(k)]
