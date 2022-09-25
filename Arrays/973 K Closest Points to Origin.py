class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      # 727 ms
        results = sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])
        return results[:k]
            
# 1492 ms
#         l = []
#         for i in points:
#             l.append((i[0]**2+i[1]**2)**0.5)
#         sorted_zipped_lists = sorted(zip(l, points))
#         sorted_list1 = [element for _, element in sorted_zipped_lists]
#         return (sorted_list1[:k])
            
