array = [100,65,98,23,9,12]

minVal = array[0]

for i in array:
    if i < minVal:
        minVal = i

print(f"Lowest Value : {minVal}")
