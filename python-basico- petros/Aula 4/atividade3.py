"""3.	Faça um script que mostre os números 
pares em um intervalo definido pelo usuário"""

i = 0

intervalo1 = int(input("Digite um intervalo"))
intervalo2 = int(input("Escreva o final"))

if intervalo1 < intervalo2:
    while intervalo1 <= intervalo2:
        if intervalo1 %2==0:
            print(intervalo1)
        intervalo1 += 1
elif intervalo2 < intervalo1:
    while intervalo2 <= intervalo1:
        if intervalo2 %2==0:
            print(intervalo2)
        intervalo2 += 1
        
else:
    print("ta brincando mt ja")


