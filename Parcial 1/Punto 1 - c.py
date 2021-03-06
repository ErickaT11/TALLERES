#Problema: Sumar los n^2 primeros números naturales al cuadrado.

def suma(n):
    auxiliar = 0
    x = 0
    for i in range(n*n):
         auxiliar = i*i
         x = x+auxiliar
    return x
    
resultado = suma(8)
print(resultado)



#Valor de n                        Resultado
#  2                                   14
#  4                                   1240
#  6                                   14910
#  8                                   85344
#  10                                  328350          
#  100                                 333283335000
#  1000                                333332833333500000
  
  
#  Análisis de complejidad:
  
#  El análisis se realiza a través del método de inspección.
#  A pesar de ser n^2 iteraciones, es lo mismo que tener un ni > n; es decir, igualmente se hace un solo recorrido.
#  Las asignaciones dentro del ciclo (el número natural x por si mismo), representa 2i operaciones; sin embargo, en general,
#  la complejidad es:
  
#  O(n)
