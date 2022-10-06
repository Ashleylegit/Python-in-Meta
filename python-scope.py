#Scoping in Python:
#General and Local Scoping

#global scope
my_scope = 20

def myn():
    local_v =40
    print('Access to Global', my_scope)

    myn()