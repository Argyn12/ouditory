l = [545, 23, 12, 4123, 11, 454, 86, 498, 78, 97]

def Find_max(l):
    sum = 0
    for i in l:
        sum+=i
    return sum
print(Find_max(l))