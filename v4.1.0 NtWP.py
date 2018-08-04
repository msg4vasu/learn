digiteen = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
digidouble = ['ones','tens','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
print "This machine handles only 3 digit positive integers."
print "This machine converts numbers into word form"
while True:
  hund=int(raw_input('Enter the hundreds digit.'))
  tens=int(raw_input('Enter the tens digit.'))
  ones=int(raw_input('Enter the ones digit.'))
  if tens==0: # Is the tens digit 0?
      d=digiteen[ones]
  if tens==1: # Is the tens digit 1?
      n=ones+10
      d=digiteen[n]
  if tens>=2: # Is the tens digit 2 or greater?
      if ones!=0:
          d=digidouble[tens]+' '+digiteen[ones]
      else:
          d=digidouble[tens]
  if hund==0:
      print d
  else:
      print digiteen[hund],'hundred and',d
  status= raw_input('Type end, to not repeat the program, type anything else to repeat the program')
  if status=='end':
    break
  
                    
