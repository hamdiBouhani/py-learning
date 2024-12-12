squares = []
for i in range(10):
    squares.append(i**2)


for item in squares:
    print(item)
    
# pythonic way 
squares =[i**2 for i in range(11,20)]
for item in squares:
    print(item)
    
    
# evens
evens=[i for i in range(10) if i%2==0]
print(evens)

# dictionary of numbers and their squares
squares = {i:i**2 for i in range (10)}
print(squares)

#set of unique values
unique_squares={i**2 for i in range(10)}
print(unique_squares)

point=(1,2)
x,y=point

print(x,y)

pairs=[(1,'a'),(2,'b'),(3,'c')]
for number,letter in pairs:
    print(number,letter)
    
# zip combine lists
names =['Alice','Bob','Charlie']
scores=[85,92,78]

for name,score in zip(names,scores):
    print(f"{name} scored {score}")