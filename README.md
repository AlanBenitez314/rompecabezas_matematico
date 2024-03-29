# Rompecabezas matemático

Resolución de un problema cómputo

Esta es una breve explicación y documentación de como afrontar el siguiente problema:

¿Cuál sería el resultado de ejecutar el siguiente pseudocódigo?

```
función solucionarRompecabezas(N) {
.var_A = 1
.var_B = 1
.var_C = 1
.var_D = 1

.para i en el rango de 1 a N {
..resultado = 3 * var_D + 1 * var_C + 4 * var_B + 1 * var_A
..var_A = var_B
..var_B = var_C
..var_C = var_D
..var_D = resultado
.}

.devolver var_D % 10000000000 // últimos 10 dígitos de var_D
}

mostrar solucionarRompecabezas(10)
mostrar solucionarRompecabezas(100)
mostrar solucionarRompecabezas(pot(2023, 100)) // 2023 elevado a la 100

Salida
902441
8042318513
??
```

Una representación en python del pseudocódigo sería:

```python
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
```

El computo de este programa es muy sencillo, queda extremadamente clara la relación de recurrencia que se tiene. Sin embargo observemos los tiempos de ejecución para la siguiente iteración:

```python
for i in range(1,7):
    t1 = time.time()
    x = solucionarRompecabezas(10**i)
    t2 = time.time()
    print("solucionarRompecabezas(10**",i,") : ", x, "tiempo: ", t2-t1)
```



```
solucionarRompecabezas(10** 1) :  902441 tiempo:  0.0
solucionarRompecabezas(10** 2) :  8042318513 tiempo:  0.0
solucionarRompecabezas(10** 3) :  5707087785 tiempo:  0.0
solucionarRompecabezas(10** 4) :  6670425081 tiempo:  0.02800154685974121
solucionarRompecabezas(10** 5) :  3336919761 tiempo:  1.7640049457550049
solucionarRompecabezas(10** 6) :  1840355025 tiempo:  194.54952764511108
```	

Como podemos observar, el tiempo de ejecución aumenta significativamente, por lo que se hace necesario buscar una forma de optimizar el cálculo de la función `solucionarRompecabezas`.

## Perspectiva matemática

Notemos que la sucesión se puede representar matemáticamente como:

```
an+4 = 3 * an+3 + 1 * an+2 + 4 * an+1 + 1 * an 
```
Se puede fácilmente observar que la sucesión es una sucesión lineal de 4 términos, por lo que podemos abordar el cálculo de la sucesión de forma matricial.

De la siguiente manera:

![Sistema matricial](/imagenes/matriz_sistema.png)

Siendo alpha_0, alpha_1, alpha_2, alpha_3 los valores que acompañan los coeficientes de la ecuación de recurrencia.

Es decir alpha_0 = 1, alpha_1 = 4, alpha_2 = 1, alpha_3 = 3

