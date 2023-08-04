"""
4.	Faça um script que leia dois valores 
positivos e mostre a soma dos números ímpares entre eles.
"""

i = 0
soma = 0

n1 = int(input("Escreva um valor"))
n2 = int(input("Escreva outro valor"))

if n1 > 0:
    while n1 <= n2:
        if n1 %3 == 0:
            soma = n1 +1
        elif n2 %3== 0:
            soma = n2 +1
else:
    print("tente outra vez")

        