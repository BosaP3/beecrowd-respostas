def separar_valores(string, sinal):
    string = string.split(sinal)
    if sinal == '/':
        [N1, D1, N2, D2] = string
    else:
        [N1, D1] = string[0].split('/')
        [N2, D2] = string[1].split('/')

    return [int(N1), int(D1), int(N2), int(D2)] # VALORES DOS NUMERADORES E DENOMINADORES

def calcula_mdc(numerador, denominador):
    if denominador == 0:
        return numerador
    else:
        return calcula_mdc(denominador, numerador % denominador)
    
def resultado_final(numerador, denominador, mdc):
    numerador_simplificado = numerador // mdc
    denominador_simplificado = denominador // mdc

    if denominador < 0:
        numerador *= -1
        denominador *= -1
    
    if denominador_simplificado < 0:
        numerador_simplificado *= -1
        denominador_simplificado *= -1

    print(f'{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}')

#----------------------------------------------------------------

n = int(input())

for _ in range(n):
    string = input()

    # CASO SOMA DE FATORIAIS 
    if '+' in string:
        N1, D1, N2, D2 = separar_valores(string, '+')

        #soma: (N1*D2 + N2*D1)
        numerador = (N1 * D2) + (N2 * D1)
        denominador = D1 * D2

        mdc = calcula_mdc(numerador, denominador) # calcula o MDC dos valores

        resultado_final(numerador, denominador, mdc)
        
    # CASO SUBTRAÇÃO DE FATORIAIS
    elif '-' in string:
        N1, D1, N2, D2 = separar_valores(string, '-')

        #subtracao: (N1*D2 - N2*D1) / (D1*D2)
        numerador = (N1 * D2) - (N2 * D1)
        denominador = D1 * D2

        mdc = calcula_mdc(numerador, denominador) # calcula o MDC dos valores

        resultado_final(numerador, denominador, mdc)

    # CASO MULTIPLICACAO DE FATORIAIS
    elif '*' in string:
        N1, D1, N2, D2 = separar_valores(string, '*')

        #multiplicacao: (N1*N2) / (D1*D2)
        numerador = N1 * N2
        denominador = D1 * D2

        mdc = calcula_mdc(numerador, denominador) # calcula o MDC dos valores

        resultado_final(numerador, denominador, mdc)

    # CASO DIVISAO DE FATORIAIS
    else:
        N1, D1, N2, D2 = separar_valores(string, '/')

        #divisao:  (N1*D2) / (N2*D1)
        numerador = N1 * D2
        denominador = N2 * D1

        mdc = calcula_mdc(numerador, denominador) # calcula o MDC dos valores

        resultado_final(numerador, denominador, mdc)
