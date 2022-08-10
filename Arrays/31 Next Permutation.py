
class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = n - 2
        while k >= 0:
            if arr[k] < arr[k + 1]:
                break
            k -= 1
        if k < 0:
            arr.sort()
        else:
            for l in range(n - 1, k, -1):
                if arr[l] > arr[k]:
                    break
            arr[l], arr[k] = arr[k], arr[l]
            arr[k + 1:] = reversed(arr[k + 1:])
