"""
12.	Faça um Script em Python que solicite ao usuário informar uma quantidade de dias,
 horas, minutos e segundos.
   Em seguida, converta tudo para segundos"""

dias = int(input("Informe os dias"))
horas = int(input("Informe as horas"))
min = int(input("Informe os minutos"))
seg = int(input("INforme os segundos"))


print(f"O valor de{dias} em minutos é:{dias*86400}")
print(f"O valor de{horas} em minutos é:{horas*3600}")
print(f"O valor de{min} em minutos é:{min/60}")
print(f"O valor de{seg} em minutos é:{seg}")