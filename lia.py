# lia

from scipy.stats import binom

def lia(k, n):
    a = 2**k
    p = 0.25
    return 1 - binom.cdf(n - 1, a, p)  #P(X >= N) = 1 - P(X < N)


k = 6  
n = 15 
print(round(lia(k, n),3))
