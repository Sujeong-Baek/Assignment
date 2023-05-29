# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import defaultdict
def solution(weights):
    answer = 0
    multiple2idxweights = defaultdict(list)    
    for idx, w in enumerate(weights):
        idxweights=set() # {} : dictionary
        for dis in [2,3,4]:
            multiple = w * dis
            if multiple in multiple2idxweights:
                for idxweight in multiple2idxweights[multiple]:
                    idxweights.add(idxweight)
            multiple2idxweights[multiple].append((idx, w))
        answer+=len(idxweight)
    return answer

# [100,200,100, 100]
# answer=6
# set={(0,100)(2,100)(1,200)}
# 200:[(0,100)(2,100)]
# 300:[(0,100)(2,100)]
# 400:[(0,100),(1,200)(2,100)]




# [100,180,360,100, 540, 270]
# (100, 100)
# (180, 360)
# (180, 270) (3,2)
# (270, 360) [540, 810, 1080] [720, 1080, 1440]
# 540 [540,1080,1620]
# 1080 -> [360,540]


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        num2idx=dict()
        for idx, num in enumerate(nums):
            if target-num in num2idx:
                return [num2idx[target-num], idx]
            num2idx[num]=idx


        # for idx1, num1 in enumerate(nums[:-1]):
        #     for idx2, num2 in enumerate(nums[idx1+1:], idx1+1):
        #         if num1+num2 == target:
        #             return [idx1, idx2]


[2,7,11,15] , 9
# num -> idx
# num2idx[2] = 0

# [3,2,4], 6 >> []
[1,2]

[3,3], 6
[0,1]


