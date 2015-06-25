fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
numf = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    num = line[line.find(':')+1:].strip()
    numf = numf + float(num)
print "Average spam confidence:",numf/count
