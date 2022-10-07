# Sets in Python 
# helps to restore different types of data in different formats.

set_m = {2, 4, 6, 8, 10}
#set_m.add(12)

#set_m.discard(4)

#print(set_m)

set_z = {5, 10, 15, 20, 25}

print(set_m.union(set_z))
           #OR
print(set_m | set_z )

# Sets do not accept duplicate values

print(set_m.difference(set_z))
print(set_z - set_m)
print(set_m.symmetric_difference(set_z))
print(set_m ^ set_z)

