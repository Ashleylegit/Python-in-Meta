#Looping Constructs
#Looping is the action of action.
#Two different constructs:
# For loop, while loop

#favorites = ['chocolate ice-cream', 'churros', 'black forest cake', 'Cheese cake']

#for idx, item in enumerate(favorites):
    #print('I like this', item)
    #print ('One of my favorite desert is', item)

favorites = ['chocolate ice-cream', 'churros', 'black forest cake', 'Cheese cake']

count = 0

while count < len(favorites):
       print('I like this desert', favorites[count]);
       count += 1