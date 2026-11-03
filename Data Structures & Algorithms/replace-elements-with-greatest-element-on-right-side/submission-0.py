class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        for i in range(len(arr) - 1, -1, -1):
            #first case ^
            if arr[i] > max:
                temp = max
                max = arr[i]
                arr[i] = temp
            else:
                arr[i] = max
        arr[len(arr)-1] = -1
        return arr