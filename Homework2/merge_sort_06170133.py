class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        answer = [] #創一個空的list裝答案
        if len(nums) <= 1: #如果list等於或小於1，就直接回傳該list
            return nums
        mid = int(len(nums)/2) #先找出中間值在哪，準備拆解list
        leftlist = self.merge_sort(nums[:mid]) #mid左邊的index放在左邊的list
        rightlist = self.merge_sort(nums[mid:]) #mid+右邊的index放在右邊的list


        while (len(leftlist) > 0) or (len(rightlist) > 0):
            if len(leftlist) > 0 and len(rightlist) > 0: #如果兩個list長度都大於0就跑這個
                if leftlist[0] > rightlist[0]: #如果左邊第一個數大於右邊第一個，
                    answer.append(rightlist[0]) #把右邊第一個append到答案的list裡
                    rightlist.pop(0) #把append進去的數從原本的list pop掉
                else :
                    answer.append(leftlist[0]) #else的話就是把左邊的第一個append到答案list裡
                    leftlist.pop(0) #把append進去的數從原本的list pop掉
                    
            elif len(rightlist) > 0: #如果只有右邊的list還有東西就跑這個
                for i in rightlist:
                    answer.append(i) #append出他的數
                    rightlist.pop(0) #pop掉
                    
            else: #如果是左邊list還有東西就跑這邊
                for i in leftlist:
                    answer.append(i) #append出他的數
                    leftlist.pop(0) #pop掉

        return answer
