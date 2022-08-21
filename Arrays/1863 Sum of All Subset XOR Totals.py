class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def get_bit(num, bit):
            temp = (1 << bit)
            temp = temp & num
            if temp == 0:
              return 0
            return 1

        def get_all_subsets(v, sets):
            subsets_count = 2 ** len(v)
            for i in range(0, subsets_count):
              st = []
              for j in range(0, len(v)):
                 if get_bit(i, j) == 1:
                    st.append(v[j])
              sets.append(st)
        subsets = []
        get_all_subsets(nums, subsets);
        mx=0
        for i in subsets:
            c=0
            for j in range(len(i)):
              c=c^i[j]
            mx=mx+c
        return(mx)
        
