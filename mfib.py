# mfib

def mfib(n, m):
    rabbits = [0] * m  #Array to store the rabbits, that only has "m" spots
    rabbits[0] = 1   
    
    for month in range(1, n):
        new_born = sum(rabbits[1:])  #Excluding newborn pairs
        rabbits = [new_born] + rabbits[:-1]   #Dropping the old ones
    
    return sum(rabbits)


print(mfib(91, 20))  
