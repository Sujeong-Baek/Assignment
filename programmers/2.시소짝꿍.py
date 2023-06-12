# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import defaultdict, Counter
def solution(weights):
    answer = 0
    weight2count=Counter(weights)
    for weight, count in weight2count.items():
        for l1,l2  in [[2,3],[2,4],[3,4]]:
            # if weight*l1/l2 in weight2count:
            answer+= weight2count[weight*l1/l2]*count
        answer+=count*(count-1)/2
    return answer

    multiple2idxs = defaultdict(set)  
    for idx, w in enumerate(weights):
        idxs=set() # {} : dictionary
        for dis in [2,3,4]:
            multiple = w * dis      
            idxs = idxs.union(multiple2idxs[multiple])
            multiple2idxs[multiple].add(idx)
        answer+=len(idxs)
    return answer

# 2m,3m,4m
# 100, 100,
# 100, 2m, : 200/3kg,3m
# 100, 2m : 50, 4m
# 100, 3m : 300/4,4
# 100, 3m : 150 ,2m
# 100, 4m : 200, 2m
# 100, 4m : 400/3, 3m

# [100,100,100,300,200]
# {100:3, 200:1,300:1}
# 200,300,400
# 3 * 3 + 3 = 12
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


