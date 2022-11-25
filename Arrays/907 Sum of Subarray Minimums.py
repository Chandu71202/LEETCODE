class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        min_stack = [] # (min, count, total_sum)
        
        for i in range(len(arr)):
            num = arr[i]
            count = 1
            while min_stack and num <= min_stack[-1][0]:
                count += min_stack.pop()[1] # count how many previous mincan be replaced by this new min
            if min_stack:
                min_stack.append((num, count, min_stack[-1][2] + num*count))
            else:
                min_stack.append((num, count, num*count))
            res += min_stack[-1][2]

        return res % (10 ** 9 + 7)
