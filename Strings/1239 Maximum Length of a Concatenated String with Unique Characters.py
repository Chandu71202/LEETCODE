class Solution:
    def maxLength(self, arr: List[str]) -> int:
        concat = [""]
        def checkunique(s):
            return len(list(set(s))) == len(s)
        maxlen = 0
        for string1 in arr:
            for string2 in concat:
                candidate = string2 + string1
                if checkunique(candidate):
                    maxlen = max(maxlen, len(candidate))
                    concat.append(candidate)
        return maxlen
#         def get_bit(num, bit):
#             temp = (1 << bit)
#             temp = temp & num
#             if temp == 0:
#               return 0
#             return 1

#         def get_all_subsets(v, sets):
#             subsets_count = 2 ** len(v)
#             for i in range(0, subsets_count):
#               st = set([])
#               for j in range(0, len(v)):
#                  if get_bit(i, j) == 1:
#                     st.add(v[j])
#               sets.append(st)
#         subsets = []
#         get_all_subsets(arr, subsets);
#         maxi=0
#         for i in subsets:
#             s=""
#             for j in i:
#                 s=s+j 
#             if(len(set(s))==len(s) and (maxi<len(s))):
#                 maxi=len(s)
#         return(maxi)
            
                
        
