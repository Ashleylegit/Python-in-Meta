# This is a simple code to calculate a bill after tax is added.

#bill = 180.00


#tax_rate = 10

#total_tax = (bill * tax_rate) / 100.00

#total_bill = (bill + total_tax)

#print('total tax', total_tax)
#print ('bill', bill)
#print ('total bill', total_bill)

# OR
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

# Code below needs to be examined more, what I am trying to accomplish is getting the total bill with tax included using the def function. It is already done in the eample up above!

def total_bill(bill, tax_rate):
    return round((bill + tax_rate), 2)

print('total_tax', calculate_tax(900.00, 10))

print('bill total', total_bill(900.00, 10) )