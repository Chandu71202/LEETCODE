class Solution:

#   T.C = 103ms

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        c = defaultdict(int)

        ans = []

        left = []

        for num in arr2:

            if num in arr1:

                c[num]=arr1.count(num)

        

        for key,value in c.items():

            ans+=[key]*value

            for _ in range(value):

                arr1.remove(key)

        return ans+sorted(arr1)

        

   

# T.C = 105ms

# class Solution:

#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

#         l = []

#         for i in arr1:

#             if i not in arr2:

#                 l.append(i)

#         l.sort()

#         d = {}

#         for i in arr2:

#             d[i]=arr1.count(i)

#         ans = []

#         for i,j in d.items():

#             a = [i]*j

#             ans+=a

#         return ans+l
