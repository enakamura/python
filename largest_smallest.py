largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        numi = int(num)
    except:
        print('Invalid input')
        continue
    if smallest == None:
        smallest = numi
    if numi < smallest:
        smallest = numi
    if numi > largest:
        largest = numi

print "Maximum is",largest
print "Minimum is",smallest
