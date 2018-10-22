class Solution(object):
    def summaryRanges(self,nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        prev = nums[0]
        curr  = nums[1]
        diff= prev - curr
        prev_diff = None
        actual_diff = -100
        start = nums[0]
        end = None
        output = []
        for item in range(1,len(nums)) :
            curr = nums[item]
            diff = prev - curr
            actual_diff = diff
    
            if diff < -1 and prev_diff == -1:
                end = prev
                print("start",start,end)
                if start!= end:
                    output.append(str(start)+"->"+str(end))
                else:
                    output.append(str(start))
                start = curr
                diff = -1

            elif diff < -1 and prev_diff != -1:
                output.append(str(prev))
                end = None
                start = curr

            prev = nums[item]
            prev_diff = diff

        print("end of loop",actual_diff,prev_diff)
        if actual_diff == -1 and prev_diff == -1:
            end = prev
            print("starting", start, end)
            output.append(str(start) + "->" + str(end))
        else:
            output.append(str(prev))
        return output