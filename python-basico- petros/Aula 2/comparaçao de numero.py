#leia dois numeros inteiros e mostre somente o menor valor

num1 = int(input("escreva um valor"))
num2 = int(input("Escreva outro valor diferente"))

if num1 < num2:
    print(f"{num1} é menor")
elif num1 == num2:
    print("TA ACHANDO Q SOU PALHAÇO?")
else: 
    print(f"{num2} é maior")