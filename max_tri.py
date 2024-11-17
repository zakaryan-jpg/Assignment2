# Hackerrank challange 1
#Max parameter triangle 

n = 5
sticks = [0]*n

values = "1 1 1 3 3"
values = list(map(int, values.split()))
sticks = values 

def max_tri(sticks,n):
    sticks.sort(reverse=True)
    
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            triangle = sorted([sticks[i], sticks[i + 1], sticks[i + 2]]) 
            return triangle
        else:
            return [-1]
    

print(max_tri(sticks,n))


