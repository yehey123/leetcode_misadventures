class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1[:]
        while nums2:
            num2 = nums2.pop()
            print('Number to be popped: ', num2)
            copy = merged[:]
            if copy:
                while copy:
                    num1 = copy.pop()
                    if num1<num2:
                        break
                if num1<num2:
                    left = merged[:len(copy)+1]
                    right = merged[len(copy)+1:]
                    merged = left + [num2] + right
                else:
                    merged = [num2] + merged
                # print('Merged list: ', merged)
            else:
                merged.append(num2)
        # print((merged[int(len(merged)/2)] + merged[int(len(merged)/2)+1])/2)
        if len(merged) % 2:
            return merged[int(len(merged)/2)]
        else:
            return (float(merged[int(len(merged)/2)-1]) + float(merged[int(len(merged)/2)]))/2

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """