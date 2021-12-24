class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x = len(nums1)-1;i=m-1;j=n-1
        while(x>=0):
            if(j<0):
                break
            if(i<0):
                nums1[x]=nums2[j]
                x-=1;j-=1
            else:
                if(nums1[i]>nums2[j]):
                    nums1[x]=nums1[i]
                    x-=1;i-=1
                else:
                    nums1[x]=nums2[j]
                    x-=1;j-=1