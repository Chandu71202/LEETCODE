class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d1={}
#         d2={}
#         set1=list(set(ransomNote))
#         set2=list(set(magazine))
#         for i in set1:
#             d1[i] = ransomNote.count(i)
#         for i in set2:
#             d2[i] = magazine.count(i)
        
#         print(d1)
#         print(d2)
        
#         for i in d1:
#             if i in d2:
#                 print(d2[i])
#                 print(d1[i])
#                 if(d1[i]!=d2[i] and d2[i]<d1[i]):
#                     return False
#             else:
#                 return False
#         return True
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
