# Collatz Sequence
# n = n/2 if even
# n = 3n + 1 if odd
# Goma 22/01/2017

dicti = {}   # Dictionary with the length of collatz sequences
def generateCollatzSequence(n):
    if n in dicti:
        return dicti[n]
    else:
        if n == 1:
            return 1

        if n % 2 == 1:
            nextNumber = 3 * n +1
        else:
            nextNumber = n / 2
        dicti[n] = 1 + generateCollatzSequence(nextNumber)
        return dicti[n]

#Pre Computation for lengths
dicti2 = {}
mPos = 0
mValue = 0
for j in range(1,500000):
    t = generateCollatzSequence(j)
    if t >= mValue:
        mValue = t
        mPos = j

    dicti2[j] = mPos


n = int(raw_input())
for i in xrange(n):
    num = int(raw_input())
    print dicti2[num]
