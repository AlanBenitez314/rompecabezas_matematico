import time
N=2023**100

def multiplicar_matrices_con_modulo(matriz_a, matriz_b, modulo):
    numero_filas_a, numero_columnas_a = len(matriz_a), len(matriz_a[0])
    numero_columnas_b = len(matriz_b[0])
    resultado = []
    for i in range(numero_filas_a):
        fila_resultado = []
        for j in range(numero_columnas_b):
            suma = 0
            for k in range(numero_columnas_a):
                suma = suma + (matriz_a[i][k] * matriz_b[k][j])
                suma = suma % modulo
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def elevar_matriz_modulo(matriz, potencia, modulo):
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
        potencia = potencia // 2
    return resultado

def solucionarRompecabezas(numero_iteraciones, modulo=10000000000):
    matriz = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 4, 1, 3]
    ]

    valores_iniciales = [1, 1, 1, 1]
    valores_finales = elevar_matriz_modulo(matriz, numero_iteraciones, modulo)
    resultado_final = 0
    for i in range(4):
        resultado_final = resultado_final + (valores_finales[3][i] * valores_iniciales[i])
        resultado_final = resultado_final % modulo
    
    return resultado_final

t1 = time.time()
x = solucionarRompecabezas(N)
t2 = time.time()
print("solucionarRompecabezas(pot(2023, 100)): ", x, "tiempo de cómputo: ", t2-t1)
