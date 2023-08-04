"""
10.	Faça um Script em Python que solicite ao usuário digitar 2 números.
 Em seguida, 
imprima o total com casas decimais da divisão e o total inteiro (sem casas decimais): """


n1 = float(input("Escreva um numero"))
n2 = float(input("Escreva outro numero"))

print(f"O total da divisao é: { n1/n2}")
print(f"O total arredondado é: {n1/n2:.0f}")