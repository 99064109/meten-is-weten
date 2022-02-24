MINIMAAL_DIEREN_ERVARING = 4
MINIMAAL_JAAR_JONGLEREN = 5
MINIMAAL_JAAR_ACROBATIEK = 3
LENGTE = 150
GEWICHT = 90
SNOR_BREEDTE = 10
KRULHAAR_LENGTE = 20 

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+ Sollicitatie formulier Circusdirecteur voor Circus HotelDeBotel +' )
print('+                    Nu volgt er een vragenlijst.                 +')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

naam = input('Wat is uw naam? ')
leeftijd = int(input('Hoeveel jaar bent u? '))
hobby = input("Wat zijn uw hobby's? ")
dierenErvaring = int(input('Hoeveel jaar ervaring heeft u met dieren? '))
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? '))
acrobatiek = int(input('Hoeveel jaar ervaring heeft u met acrobatiek? '))
lengte = int(input('Wat is uw lengte in centimeters? '))
gewicht = int(input("Hoeveel weegt u in kilo's? "))
sport = input('Doet u aan een sport? zo ja wat voor sport beoefend u? ')
mbo = input('Bent u in het bezit van een mbo niveau 4 ondernemen diploma? ')
vrachtwagen_rijbewijs = input('Bent u in het bezit van een geldig vrachtwagen rijbewijs? ')
hoelang_rijbewijs = input('Hoeveel jaar heeft u uw vrachtwagen rijbewijs al? ')
certificaat = input('Bent u in het bezit van een certificaat Overleven met gevaarlijk personeel? ')   
hoed = input('Bent u in het bezit van een hoge hoed? ')
man_of_vrouw= input('Bent u een man of vrouw? ')
if man_of_vrouw == 'man':
    snor = input('heeft u een snor? ')
    if snor == 'ja':
        snor_breedte = int(input('Hoe breedt is uw snor in centimeters? '))
else:
    krullend_haar = input('Heeft u rood krullend haar? ')           
    if krullend_haar == 'ja':
        krulhaar_lengte = int(input('Hoelang is uw krulhaar in centimeters? '))
    
if dierenErvaring < MINIMAAL_DIEREN_ERVARING and jongleren < MINIMAAL_JAAR_JONGLEREN and acrobatiek < MINIMAAL_JAAR_ACROBATIEK:
    print('helaas u bent niet geschikt om hier te werken.')
else:
    if lengte < LENGTE or gewicht < GEWICHT or mbo == 'nee' or vrachtwagen_rijbewijs == 'nee' or certificaat == 'nee'  :
        print('Helaas u bent niet geschikt')
    else:

        if man_of_vrouw == 'man':
            if snor == 'nee':
                print('u mag hier niet werken ')
            elif snor_breedte < SNOR_BREEDTE:
                print('U mag hier niet werken ')
            else:
                print('U bent geschikt om hier te werken ')
    
        elif man_of_vrouw == 'vrouw':
            if krullend_haar == 'nee':
                print('U mag hier niet werken ')
            elif krulhaar_lengte < KRULHAAR_LENGTE:
                print('U mag hier niet werken ')
            else:
                print('U bent geschikt om hier te werken ')
    

   

