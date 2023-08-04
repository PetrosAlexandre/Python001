# #Estrutura de repeticao while (cont)
# #leia 5 numeros e mostre a soma de todos os valores informados

# """i = 0
# a = 0
# b = 25

# while i<=5:
#     num = float(input("Informe um valor: "))
#     soma = soma+num
#     i += 1
# print(f"O resiltado da soma é: {soma}")"""

# #leia 2 valores(inteiros ) e mostre a soma do intervalo entre

# v1 = int(input("Escreva um valor inicial: "))
# v2 = int(input("Informe o valor final: "))
# soma = 0

# if v1 < v2: 
#     while v1 <=v2:
#         soma += v1
#         v1 +=1
#     print("O resultado é: ", soma)
# elif v2 <v1:
#     while v2 <= v1:
#         soma += v2
#         v2+=1
#     print("O resultado é:", soma)
# else:
#     print("os valores sao iguais = (")
    
# soma 5 valores positivos informados pelo usuario

# soma = 0
# i = 1

# while i <= 5:
#     valor = float(input("Escreva um valor"))
#     if valor < 0:
#         continue
#     i +=1 
#     soma += valor
# print("O total é : ",soma)

#somar os 5 valores negativos informados pelo usuario

# soma = 0
# i = 1

# while i <= 5:
#     valor  = float(input("Digite um valor negativo"))
#     if valor >= 0:
#         print("Que q há gaguinho")
#         break #pausa o codigo
#     i+=1
#     soma +=valor #acumula os numeros
# print("O valor total é: ", soma)

#leita 3 notas e mostre a media, caso seja digitado um valor negativo ou acima de 10 sera solicicitado
#um novo valor

soma = 0 
i = 1
media = 0
while i <= 3:
    nota = float(input("Escreva  a nota"))
    if nota < 0:
        print("Tente novamente")
        continue
    elif nota > 10:
        print("Tente novament")
        continue
    else:
        soma += nota
        media = soma / i
        i +=1
print(f"A media é: {media} ")
print(f"A soma das notas é: {soma}")


