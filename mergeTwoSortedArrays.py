class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1, nums2, and the final position in nums1
        p1 = m - 1      #Start at the last value for nums1 that isn't going to be replaced
        p2 = n - 1      #Start at the last value for nums2
        p = m + n - 1   #Start at last index for nums1

        #Traverse from the back of nums1 and nums2
        while p1 >= 0 and p2 >= 0:
            #print(nums1)
            #print(nums1[p1])
            #print(nums2[p2])
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        #If there are any remaining elements in nums2, copy them
        #If nums2 contains more values than nums1, this will be used
        while p2 >= 0:
            #print("second while")
            #print(nums1)
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
            
        #print(nums1)