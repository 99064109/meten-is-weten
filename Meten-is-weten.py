a = int(input("Voer een getal in: ")) 
b = int(input("Voer een getal in: "))

if a > b:
    max = a
    min = b
    print('a is groter dan b')
elif a < b:
    min = a
    max = b
    print('a is het kleinste getal')
else: 
    print('a en b zijn even groot') 
    min = a
    max = a
print('Het minimum is: '+str(min))
print('Het maximum is: '+str(max))
