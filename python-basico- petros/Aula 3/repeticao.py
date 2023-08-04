#Estrutura de repeticao while

vlr1 = int(input("Escreva um valor"))
vlr2 = int(input("Escreva um valor"))

if vlr1 < vlr2:
    i = vlr1

    while i<=vlr2:
        print(i)
        i = i +1


elif vlr2 <vlr1:
    i = vlr2

    while i<=vlr1:
        print(i)
        i = i +1
else:
    print("Ta doido cara?")

