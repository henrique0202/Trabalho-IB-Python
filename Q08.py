def calculadora(num1,num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "indefinida (divisao por 0 nao e permitida)"
    return soma, subtracao, multiplicacao, divisao
num1 = int(input("digite o primeiro numero inteiro:"))
num2 = int(input("digite o segundo numero inteiro:"))
soma, subtracao, multiplicacao, divisao = calculadora(num1,num2)
print(f"a soma de {num1} e {num2} e: {soma}")
print(f"a subtracao de {num1} e {num2} e: {subtracao}")
print(f"a multiplicacao de {num1} e {num2} e: {multiplicacao}")
print(f"a divisao de {num1} e {num2} e: {divisao}")