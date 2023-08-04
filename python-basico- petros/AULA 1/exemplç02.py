valor1 = 45
valor2 = 258.45

# operadores aritmeticos
print("soma:" ,valor1+valor2)
print("subtraçao:",valor1-valor2)
print("multiplicaçao:" ,valor1*valor2)
print("divisao:", valor1/valor2)
print(f"Divisao com 2 casas: {valor1/valor2: .2f}")
print(f"valor2: {valor2: .1f}")

# obter  valores do teclado
usuario = input("Informe seu nome:")
print(f"Seu usuario é:{usuario}")
idade = int(input("Informe sua idade: "))
# mostrar o dobro da idade
print(f"O dobro da sua idade é: {idade * 2:.0f}")
# mostrar os tipos de dados das variaveis

print("idade: ", type(idade))
print("usuario: ", type (usuario))
print("-",*20)
valor_curso = float(input("informe o valor pago pelo curso: "))
print(f"O valor informado foi: {valor_curso}")
#mostrar uma mensagem com 25% do valor do curso
#Parabens!!! vc ganhou <valor> de credito na proxima compra

print(f"O valor do curso com 25% de desconto é: {valor_curso*25/100}")
print(f"parabens! voce ganhou : {valor_curso*25/100}, na proxima compra")
print("-",*20)
#solicitar quantidade de parcelas do pagamento
parcelas = int(input("informe quantas percelas do pagamento"))
# mostrar o valor das parcelas sem juros
print(f"O valor de cada parcela sem juros é: {parcelas} de R${valor_curso/parcelas}")
