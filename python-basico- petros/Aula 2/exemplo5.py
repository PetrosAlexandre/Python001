#leia um valor de um produto, caso o valor seja menor do que 100 mostre a seguinte mensagem
#"Voce recebeu 5% de desconto", caso contrario
#voce recebeu10% de desconto

valor = float(input("escreva um valor"))

if valor < 100:
    print("voce recebeu 5% de desconto")
    print(f"O valor do desconto é:{100*0.05} ")
else:
    print("voce recebeu 10% de desconto")
    print(f"voce recebeu o desconto de: {100*0.10}")
