# Declaring Tuples 

my_tuple = (1, 'strings', 4.9, True)
print(my_tuple[2])

# Determing the type of tuple

print(type(my_tuple))

# Tuple also reps counts and index

print(my_tuple.count('strings'))
print(my_tuple.count('True'))
print(my_tuple.count('4.9'))

# Tuples can accept any mix of data types.

# Lets try indexing 

print(my_tuple.index(4.9))

for x in my_tuple:
    print(x)

# Anything Declared in a tuple is immutable.