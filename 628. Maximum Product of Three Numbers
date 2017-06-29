class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.quicksort(nums,0,len(nums)-1)
        if nums[0]*nums[1]>nums[-2]*nums[-3]:
            return nums[0]*nums[1]*nums[-1]
        return nums[-1]*nums[-2]*nums[-3]
    
    def quicksort(self,a,l,h):
        if l<h:
            mid = self.partition(a,l,h)
            self.quicksort(a,l,mid-1)
            self.quicksort(a,mid+1,h)
            
    def partition(self,a,l,h):
        mid = l
        val = a[l]
        for i in range(l+1,h+1):
            if a[i]<val:
                mid += 1
                if mid!=i:
                    a[mid],a[i] = a[i],a[mid]
        a[mid],a[l] = a[l],a[mid]
        return mid
        
