def determinar_periodo(hora):
    if 0 <= hora <12:
        return "manhã"
    elif 12 <= hora < 18:
        return "tarde"
    elif 18 <= hora < 24:
        return "noite"
    else:
        return "hora invalida. insira um numero de 0 a 23."
hora = int(input("digite a hora (numero inteiro de 0 a 23):"))
periodo = determinar_periodo(hora)
print(f"o horario informado é {hora} horas e corresponde ao periodo: {periodo}.")