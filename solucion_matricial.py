N = 10**6

def multiplicar_matrices_con_modulo(matriz_a, matriz_b, modulo):
    numero_filas_a, numero_columnas_a = len(matriz_a), len(matriz_a[0])
    numero_columnas_b = len(matriz_b[0])
    resultado = []
    for i in range(numero_filas_a):
        fila_resultado = []
        for j in range(numero_columnas_b):
            suma = 0
            for k in range(numero_columnas_a):
                suma += matriz_a[i][k] * matriz_b[k][j]
                suma %= modulo
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def elevar_matriz_a_potencia_con_modulo(matriz, potencia, modulo):
    resultado = []
    for i in range(len(matriz)):
        fila_identidad = []
        for j in range(len(matriz)):
            if i == j:
                fila_identidad.append(1)
            else:
                fila_identidad.append(0)
        resultado.append(fila_identidad)
    
    while potencia:
        if potencia % 2 == 1:
            resultado = multiplicar_matrices_con_modulo(resultado, matriz, modulo)
        matriz = multiplicar_matrices_con_modulo(matriz, matriz, modulo)
        potencia //= 2
    return resultado

def calcular_secuencia_con_modulo_python(numero_iteraciones, modulo=10000000000):
    matriz_transformacion = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 4, 1, 3]
    ]

    estado_inicial = [1, 1, 1, 1]
    estado_final = elevar_matriz_a_potencia_con_modulo(matriz_transformacion, numero_iteraciones, modulo)
    resultado_final = 0
    for i in range(4):
        resultado_final += estado_final[3][i] * estado_inicial[i]
        resultado_final %= modulo
    
    return resultado_final

print("mostrar solucionarRompecabezas(pot(2023, 100)) : // 2023 elevado a la 100 :", calcular_secuencia_con_modulo_python(N))