squares = []
for i in range(10):
    squares.append(i**2)


for item in squares:
    print(item)
    
# pythonic way 
squares =[i**2 for i in range(11,20)]
for item in squares:
    print(item)