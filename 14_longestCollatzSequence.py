# Collatz Sequence
# n = n/2 if even
# n = 3n + 1 if odd
# Goma 22/01/2017
lenMax     = 5000000

dicti  = [0] * lenMax   # Dictionary with the length of collatz sequences
dicti2 = [0] * lenMax   # Dictionary with the length of collatz sequences

def generateCollatzSequence(n):
    if n > lenMax and n % 2 == 1:
        return 1 + generateCollatzSequence(3 * n + 1)
    if n > lenMax and n % 2 == 0:
        return 1 + generateCollatzSequence(n/2)


    if dicti[n] != 0:
        return dicti[n]
    else:
        if n <= 1:
            dicti[n] = 1
            return 1

        if n % 2 == 1:
            nextNumber = 3 * n +1
        else:
            nextNumber = n / 2
        dicti[n] = 1 + generateCollatzSequence(nextNumber)
        return dicti[n]


biggerSoFar = 1

for i in xrange(lenMax):
    dicti[i] = generateCollatzSequence(i)
