class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        hi = len(A) -1 
        while low < hi:
            mid = (low + hi)//2 
            if A[mid] > A[mid+1] and mid > 0 and A[mid] > A[mid-1]:
                return mid
            elif A[mid] < A[mid+1]:
                low = mid +1 
            else:
                hi = mid -1 
        return hi
    