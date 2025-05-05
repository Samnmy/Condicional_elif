N1=float(input("Dame la primero nota : "))
N2=float(input("Dame la segunda nota : "))
N3=float(input("Dame la tercer nota : "))
P=(N1+N2+N3)/3
if P >= 7:
    print("Promocionado")
elif P >= 4:
    print("Regular")
else:
    print("Reprobado")    
