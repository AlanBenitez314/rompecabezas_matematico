import time

def solucionarRompecabezas(N):
    var_A = 1
    var_B = 1
    var_C = 1
    var_D = 1

    for i in range(1, N+1):
        resultado = 3 * var_D + 1 * var_C + 4 * var_B + 1 * var_A
        var_A = var_B
        var_B = var_C
        var_C = var_D
        var_D = resultado

    return var_D % 10000000000

#calcular tiempo de iteración para cada valor

for i in range(1,7):
    t1 = time.time()
    x = solucionarRompecabezas(10**i)
    t2 = time.time()
    print("solucionarRompecabezas(10**",i,") : ", x, "tiempo: ", t2-t1)