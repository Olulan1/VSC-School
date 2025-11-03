from util import read_numbers
import sys
values = read_numbers()
lenVal = len(values)
if lenVal != 0:
    min = values[0]
    max = values[0]
    total = 0
    for val in values:
        total+=val
    mean = total/lenVal
    x = lenVal %2
    if lenVal == 1:
        median = values[0]    
    elif x != 0 & lenVal != 1:
        lenVal = lenVal+1
        div = lenVal//2
        median = values[div]
    elif x == 0 & lenVal !=1 :
        div = lenVal//2
        values.sort()
        print(values)
        median = (values[div] + values[div-1])/2
        
    for val in values:
        if val > max:
            max = val
        
        if val < min:
            min = val
else:
    sys.exit("Error: no numbers provided")

print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean    = {mean:.2f}")
print(f"Median  = {median:.2f}")