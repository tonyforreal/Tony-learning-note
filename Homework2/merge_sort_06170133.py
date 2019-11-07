###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        answer = []
        if len(nums) <= 1:
            return nums
        mid = int(len(nums)/2)
        leftlist = self.merge_sort(nums[:mid])
        rightlist = self.merge_sort(nums[mid:])


        while (len(leftlist) > 0) or (len(rightlist) > 0):
            if len(leftlist) > 0 and len(rightlist) > 0:
                if leftlist[0] > rightlist[0]:
                    answer.append(rightlist[0])
                    rightlist.pop(0)
                else :
                    answer.append(leftlist[0])
                    leftlist.pop(0)
            elif len(rightlist) > 0:
                for i in rightlist:
                    answer.append(i)
                    rightlist.pop(0)
            else:
                for i in leftlist:
                    answer.append(i)
                    leftlist.pop(0)

        return answer
