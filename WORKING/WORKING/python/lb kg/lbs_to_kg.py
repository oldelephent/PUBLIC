weight = int(input('enter ur weight in digit kg or lb 50: '))
unit  = input("u want to convert in (L)bs or (K)g " )

#1 kg == 0.45 pound

if unit.upper() == 'L':
    weg = weight * 0.45
    print(f"ur weight is {weg} pound" )
    

if unit.upper() == 'K':
    weg = weight // 0.45 
    print(f"ur weight is {weg}  kilos" )
