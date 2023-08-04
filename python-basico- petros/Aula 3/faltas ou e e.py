#aplicar operadores logicos com if
#leia aqtd de faltas de um aluno e sua media final

faltas = int(input("Digite as faltas: "))

media = float(input("Informe a media final: "))

#condiçoes de reprovacao
#qtd de faltas maior do que 8 ou media menor que 7
#analisar condiçao do aluno somente se o valor das faltas for maior ou igual a zero

if faltas <0:
     print("ta negado papai")

else:
    if faltas > 8 or media <7:
        print("aluno reprovado")

        if faltas > 8 and media < 7:
            print("Voce é BURRO")
        elif faltas > 8:
            print("Voce reprovou por faltas")
        else:
            print("Voce reprovou por nota baixa")
    else:
        print("aluno aprovado")