class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-x for x in nums]

        heapq.heapify(neg_nums)
        while k>0:
            res = heapq.heappop(neg_nums)
            k -= 1
        return -res


