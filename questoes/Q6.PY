def verificar_eligibilidade(nome,idade):
    if idade >= 16:
        return f"{nome},voce pode emitir o seu titulo de eleitor."
    else:
        return f"{nome}, voce ainda nao pode emitir o seu titulo de eleitor"
nome = input("digite o seu nome:")
idade = int(input("digite a sua idade:"))
mensagem = verificar_eligibilidade(nome,idade)
print(mensagem)