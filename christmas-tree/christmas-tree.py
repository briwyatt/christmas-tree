def holidaybush(n, characters):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print(characters,end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()




hb = int(input("how tall do you want your tree to be?"))      
charcode = input("what kind of characters?")
holidaybush(hb, charcode)