# Starter code

items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except:
    print("there is no 6 in the items lists")



def divide_by(z,q):
    try:
        return z / q
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong with this division')

ans = divide_by(30,0)
print (ans)     


    
try:
        with open('file_does_not exist.txt', 'r') as file:
            print(file.read())
except:
        print("File will never be found. Bye!!")

