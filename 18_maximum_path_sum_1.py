def maxSum(S, i, depth):
    if depth == len(S)-1:
        return S[depth][i]
    else:
        maxL = S[depth][i] + maxSum(S, i, depth+1)
        maxR = S[depth][i] + maxSum(S, i+1, depth+1)
        return max(maxL, maxR)

n = int(raw_input())
for i in xrange(n):
    nums = []
    num = int(raw_input())
    for i in xrange(num):
        nums.append(map(int, raw_input().split(" ")))
    print maxSum(nums, 0, 0)
