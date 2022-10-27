n = int(input("Zadana suma: "))
a1 = b1 = 0 #a1,a2 - ciag wiekszy; b1, b2 - ciag mniejszy
a2 = b2 = 1
sumaa = sumab = 1
suma = sumaa - sumab
while True:
    if suma > n:
        b1, b2 = b2, b1 + b2
        sumab += b2

    if suma < n:
        a1, a2 = a2, a1 + a2
        sumaa += a2

    if suma == n:
        print("Istnieje ", a2, b2)
        quit()

    if n < a2: #Potem odległości jednego ciagu sumy od drugiego sa wieksze niz szukana suma i nie ma mozliwosci na nia trafic
        print("Nie istnieje")
        quit()

    suma = sumaa - sumab


