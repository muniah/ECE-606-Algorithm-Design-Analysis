import random

def RandMedianOne(A):
    arr_len = len(A)
    niterations = 0
    while True:
        niterations += 1
        i = random.randint(0, arr_len-1)
        c = 0
        for j in range(arr_len):
            if A[j] < A[i]:
                c += 1
        if c == (arr_len - 1) // 2:
            return niterations

def RandMedianTwo(A):
    arr_len = len(A)
    niterations = 0
    S = set()
    while True:
        niterations += 1
        i = random.choice([num for num in range(arr_len) if num not in S])
        c = 0
        for j in range (arr_len):
            if A[j] < A[i]:
                c += 1
        if c == (arr_len - 1) // 2:
            return niterations
        S.add(i)

def avgNIter(A):
    avgone = 0.0
    nsamples = 0
    while nsamples < 10000:
        niter = RandMedianOne(A)
        avgone = (avgone * nsamples + niter)/(nsamples + 1) 
        nsamples += 1

    avgtwo = 0.0
    nsamples = 0
    while nsamples < 10000:
        niter = RandMedianTwo(A)
        avgtwo = (avgtwo * nsamples + niter)/(nsamples + 1) 
        nsamples += 1

    return avgone, avgtwo

