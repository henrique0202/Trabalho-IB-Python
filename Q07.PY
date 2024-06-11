def calcular_media_e_situacao(nome,disciplina,nota1,nota2):
    media = (nota1 + nota2)/2
    situacao = "aprovado" if media >= 6 else "reprovado"
    return f"{nome} esta {situacao} na disciplina {disciplina}"
nome = input("digite o nome do aluno:")
disciplina = input("digite o nome da disciplina:")
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota"))
resultado = calcular_media_e_situacao(nome,disciplina,nota1,nota2)
print(resultado)