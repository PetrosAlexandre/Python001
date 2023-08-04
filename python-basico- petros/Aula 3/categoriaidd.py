"""
Leia a idade do usuario e defina a sua categoria de acordo com as seguintes informaçoes
CAtegoria- idade
sem categoria menor de 3
Infantil-3ate10
juvenil 11-17
adulto 18ate39
senior 40ate130"
acima de 130 idade invalida
"""

idd = int(input("Escreva idade"))

if idd < 3:
    print("sem categoria")
elif idd <=10:
    print("Sua categoria é infantil")
elif idd <= 17:
    print("Sua categoria é Juvenil")
elif idd <=39:
    print("adulto")
elif idd <=130:
    print("Sua categoria é Senior")
else:
    print("ta achando que a vida é brincadeira?")
