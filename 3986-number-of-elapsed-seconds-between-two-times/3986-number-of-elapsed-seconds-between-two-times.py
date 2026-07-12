class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        start_hr = int(startTime[0:2])
        end_hr = u=int(endTime[0:2])

        start_min = int(startTime[3:5])
        end_min = int(endTime[3:5])

        start_sec = int(startTime[6:])
        end_sec = int(endTime[6:])

        total_hr = end_hr - start_hr
        total_min = end_min - start_min
        total_sec = end_sec - start_sec


        return total_hr * 3600 + total_min * 60 + total_sec 