# The order in which the instructions in a programme are executed.

#Two types of control flow 
# Conditional:
# (if, else, elif(else if))
#Loops:
#(for loop, while loop)

#Example

#bill_total = 208

#discount1 = 50

#if bill_total > 200:
 #   print("bill is greater than 208")
#print ("discount to be applied")
#bill_total = bill_total -discount1

#print("Total bill"+ str(bill_total))

#bill_total = 290

#discount1 = 40
#discount2 = 50

#if bill_total > 290 and bill_total <350:
    #print("Bill is greater than 100!")
    #bill_total= bill_total - discount1

#elif bill_total > 290:
        #print('Bill is greater than 200!')
        #bill_total = bill_total - discount2

#else:
        #print("Bill is less than 100")
        #print('Total bills:'+str(bill_total))


#Light is currently off 

#current = False

#if current:
    #current = False
    #print('Turning light off')

    #if not current:
        #current = True
        # print('Turning light on')


loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))











