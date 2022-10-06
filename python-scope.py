#Scoping in Python:
#General and Local Scoping

#global scope
my_scope = 20

def myn():
    notlocal_v =40

    def myn2():
        local_v = 10
        print('Access to Scope', my_scope)
        print('Access to notlocal', notlocal_v )
    myn2()
    
myn()
