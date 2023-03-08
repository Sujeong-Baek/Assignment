def maxSubSum1(a):
  maxSum = 0
  start = 0
  end = 0
  for i in range(len(a)):
    for j in range(i, len(a)):
      sum = 0
      for k in range(i, j+1):
        sum += a[k]
      if sum > maxSum:
        maxSum = sum
        start = i
        end   = j
  return maxSum, start, end
