# Hackerrank challange 2
#Mark and toys

k = 7
prices = "1 2 3 4"
prices = list(map(int, prices.split()))

def toys(prices, k):
    prices.sort()
    sum = 0
    count = 0
    for i in prices:
        if count + i <=k:
            count += i
            sum +=1
        else:
            break
            
    return sum


print(toys(prices, k))
