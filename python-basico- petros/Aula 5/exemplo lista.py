#exemplo da funçao range()

# print(list(range(2,15)))
# print(list(range(10)))

# print(list(range(10, 100, 5)))# O 5 é o tanto de casa q vai pulando

# #loop for

# for i in range(10):
#     print(i, end = " ")
# print("\nvalor final do contador: ", i)
# print("-"*50)
# #contagem de 20 ate 30 laço for

# for j in range (20,31):
#     print(j, end =" ")
# print("valor final: ", j)

# #contagem de 10 ate o 0

# for c in range (10,-1, -1):
#     print(c,end= " ")1
# print("valor final: ",c)

#leia 5 numeros inteiros e mostre uma mensagem quando o numero for par

# for i in range(5):
#     num = int(input("Escreva um valor"))
#     if num %2 == 0:
#         print(" numeros pares")

#leia 5 numeros e  some  somente os valores impares
soma = 0
impar= 0
media= 0
for i in  range (5):
    num = int(input(f"Escreva o {i} numero"))

    if num%2 != 0:
        soma = soma + num
        impar += 1
        media = soma/ impar
print("a soma dos numeros é: ", soma)
print("A quantidade de impar: ", impar)
print(f"a media desses numeroes é : {media:.0f}")
