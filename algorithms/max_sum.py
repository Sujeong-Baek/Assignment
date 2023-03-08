def maxSubSum1(a):
    maxSum = 0
    start = 0
    end = 0
    for i in range(len(a)):  # [i, j]
        for j in range(i, len(a)):
            sum = 0
            for k in range(i, j+1):
                sum += a[k]
            if sum > maxSum:
                maxSum = sum
                start = i
                end = j
    return maxSum, start, end


# 1,2,3,4,5
# 6, -5, 3, -10, 5
# O(n**3), O(n) O(n**2)

def maxSubSum2(a):
    maxSum = 0
    start = 0
    end = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum > maxSum:
                maxSum = sum
                start = i
                end = j
    return maxSum, start, end
# O(n**2)