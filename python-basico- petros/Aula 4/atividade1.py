"""
1.	Crie um script em Python para receber dois números informados
 pelo usuário e mostrar todos números entre eles em ordem decrescente."""

n1 = int(input("escreva um numero"))
n2 = int(input("escreva um numero"))
soma = 0

while n2< n1:
    print(n2, end = " ")
    n2 =-1
if n1 < n2:
    print(n1, end= " ")
    n1 =-1