"""
7.	Faça um Script em Python que solicite a nota das 4 provas semestrais do usuário. 
Em seguida, calcule e envie para a saída padrão a média:"""

nota1 = float(input("Escreva a nota 1: "))
nota2 = float(input("Escreva a nota 2: "))
nota3 = float(input("Escreva a nota 3: "))
nota4 = float(input("Escreva a nota 4: "))

print(f"A media das notas é: {(nota1+nota2+nota3+nota4)/4}")