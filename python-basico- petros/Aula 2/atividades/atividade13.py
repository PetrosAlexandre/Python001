"""
13.	Faça um Script em Python que solicite ao usuário informar o valor de uma compra.
 Em seguida, aplique 10% de desconto e
 imprima na tela tanto o valor total como também o valor com o desconto aplicado. """

valor = float(input("Valor da compra"))
desc = valor*0.10
print(f"O valor do desconto aplicado é: R${valor*0.10}")
print(f"O valor total fica: R${valor - desc}")
