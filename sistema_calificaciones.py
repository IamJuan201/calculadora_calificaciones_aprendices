WIDTH = 80

def sistema_calificaciones():
    print("="*WIDTH)
    print("SISTEMA DE CALIFICACIONES".center(WIDTH))
    print("="*WIDTH + "\n")

    cantidad_aprendices = int(input("Ingrese la cantidad de aprendices: "))
    cantidad_calificaciones = int(input("Ingrese la cantidad de calificaciones por aprendiz: "))

    nombres = []
    promedios = []
    suma_grupo = 0

    for i in range(cantidad_aprendices):
        print(f"\nAprendiz {i + 1}")
        print("-"*WIDTH)
        
        nombre_aprendiz = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
        nombres.append(nombre_aprendiz)

        suma_notas = 0
        
        for j in range(cantidad_calificaciones):
            nota_aprendices = float(input(f"Ingrese la calificacion {j + 1} de {nombre_aprendiz}: "))
            suma_notas = suma_notas + nota_aprendices

        promedio = suma_notas / cantidad_calificaciones
        promedios.append(promedio)
        suma_grupo = suma_grupo + promedio

    print("\n" + "="*WIDTH)
    print("RESULTADOS FINALES".center(WIDTH))
    print("="*WIDTH)

    for i in range(cantidad_aprendices):
        print(f"\nAprendiz : {nombres[i]}")
        print(f"Promedio : {promedios[i]:.2f}")

        if promedios[i] >= 70:
            
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")

        print("-"*WIDTH)

    promedio_general = suma_grupo / cantidad_aprendices
    
    print(f"\nPromedio general del grupo: {promedio_general:.2f}")
    print("="*WIDTH)


sistema_calificaciones()
