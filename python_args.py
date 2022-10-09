# Key word arguments

#def sum_of (a, b):
    #return a+b

#print (sum_of(6, 9))


def sum_of(**kwargs):
    sum = 0 
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

#print(sum_of(3, 9, 89, 12, 4, 10, 7))

# Using Kwargs to calculate a bill

print(sum_of(pie= 1.99, fruitcake=2.99, coffee=1.49, tea=1.30))

# Simple way of using args and kwargs 
#Peace out 

