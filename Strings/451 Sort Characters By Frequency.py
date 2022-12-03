class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        x = count.most_common()
        s = ""
        for i,j in x:
            s+=i*j
        return s
