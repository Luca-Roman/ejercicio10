import os


ruta = os.path.abspath(os.path.dirname(__file__))
ruta_nombres_1 = os.path.join(ruta,"nombres_1.txt")
ruta_notas_1 = os.path.join(ruta,"eval1.txt")
ruta_notas_2 = os.path.join(ruta,"eval2.txt")

with open(ruta_notas_1,encoding="utf8") as arch_notas_1:
    notas_1 = arch_notas_1.read().replace(",", "").split()

with open(ruta_notas_2,encoding="utf8") as arch_notas_2:
    notas_2= arch_notas_2.read().replace(",", "").split()

with open(ruta_nombres_1,encoding="utf8") as arch_nomb_1:
    nombres_1 = arch_nomb_1.read().replace(",", "").replace("'", "").split()

def armar_lista (lista_nom, notas_1, notas_2) :
    """Genera una lista de tuplas, las tuplas contiene el nombre y la nota total del alumno"""
    i = 0
    lista_todos = []
    tup = ()
    for nom in lista_nom :
        tup = (nom, int(notas_1[i]) + int(notas_2[i]))
        lista_todos.append(tup)
        i = i + 1
    return lista_todos

def calcu_prom (list_tod) :
    """" Calcula el promedio, ingresando la lista de tuplas """
    total = 0
    cant_pibes = len(list_tod)
    for i in range(cant_pibes) :
        total = total + list_tod[i][1]
    prom =  total / cant_pibes
    return prom

def imprimir_menor_prom (list_tod, prom) :
    """" Imprime el nombre y la nota de los alumnos por debajo del promedio """
    for i in range(len(list_tod)) :
        if (list_tod[i][1] < prom) :
            nombre = list_tod[i][0]
            nota = list_tod[i][1]
            print (f"{nombre} Tuvo una suma de notas de {nota}")

lista_todos = armar_lista (nombres_1, notas_1, notas_2)
promedio = calcu_prom (lista_todos)
print(f"El promedio fue de : {promedio}")
imprimir_menor_prom(lista_todos,promedio)

