digiteen = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
digidouble = ['ones','tens','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
print "This machine handles only two digit positive integers."
print "This machine converts numbers into word form"
tens=int(raw_input('Enter the tens digit.'))
ones=int(raw_input('Enter the ones digit.'))
if tens==0: # Is the tens digit 0?
    print digiteen[ones]
if tens==1: # Is the tens digit 1?
    n=ones+10
    print digiteen[n]
if tens>=2: # Is the tens digit 2 or greater?
    if ones!=0:
        print digidouble[tens],digiteen[ones]
    else:
        print digidouble[tens]
    
