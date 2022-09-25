class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped_lists = zip(heights, names)
        sorted_zipped_lists = sorted(zipped_lists)
        sorted_list1 = [element for _, element in sorted_zipped_lists]
        return sorted_list1[::-1]
