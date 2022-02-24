kleurkaas = input('Is de kaas geel? ')
if kleurkaas == "ja":
    gaten = input('zitten er gaten in? ')
    if gaten == "ja":
        duur = input('Is de kaas belachelijk duur? ')
        if duur == "ja":
            print('Emmerthaler')
        else:
            print('Leerdammer')
    else: 
        steen = input('Is de kaas hard als steen? ')
        if steen == "ja":
            print('Pammigiano Reggiano ')
        else:
            print('Goudse kaas')
            
else:
    schimmel = input('heeft de kaas blauwe schimmel? ')
    if schimmel == "ja":
        korst = input('Heeft de kaas een korst? ') 
        if korst =="ja": 
            print('Bleu de Rochbaron')
        else:
            print("Foum d'Ambert")
    else:
        korst = input('heeft de kaas geen korst? ')
        if korst == "ja":
            print('Camembert')
        else: 
            print('Mozzarella')
