
#fibo 시간재기 
def fibo (n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo (n - 2)

import time

while True:
    nbr = int (input("Enter a number:"))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print ("Fibo(%d) = %d, time %.6f" % (nbr, fibonumber, ts))

#iterfibo 시간재기
def iterfibo(k):
    if k < 2:
         return k

    a, b = 0, 1
    for i in range (k-1):
        a, b = b, a + b

    return b

import time

while True:
    nbr = int (input("Enter a number:"))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print ("IterFibo (%d) = %d, time %.6f" % (nbr, fibonumber, ts))
