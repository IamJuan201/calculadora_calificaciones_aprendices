# Documentación, Pseudocódigo y Evidencias de Ejecución
## Sistema de Calificaciones Académicas

---

## 1. Introducción y Propósito del Código

Este script en Python permite gestionar y calcular las calificaciones de un grupo de aprendices. Su objetivo principal es automatizar la captura de múltiples notas por cada aprendiz, calcular su promedio individual, determinar su estado académico (Aprobado/Reprobado con base en una nota mínima de 70) y obtener el promedio general del grupo, presentando todo de forma organizada en consola.

---

## 2. Pseudocódigo

```text
INICIO
  Constante WIDTH = 80

  Función sistema_calificaciones():
    Imprimir título "SISTEMA DE CALIFICACIONES" centrado usando WIDTH

    Leer cantidad_aprendices (Entero)
    Leer cantidad_calificaciones (Entero)

    Crear lista vacía: nombres
    Crear lista vacía: promedios
    Inicializar suma_grupo = 0

    // Bucle para capturar datos de cada aprendiz
    Para i desde 0 hasta cantidad_aprendices - 1 hacer
      Imprimir "Aprendiz (i + 1)"
      Leer nombre_aprendiz
      Agregar nombre_aprendiz a la lista nombres

      suma_notas = 0
      // Bucle para capturar las calificaciones del aprendiz actual
      Para j desde 0 hasta cantidad_calificaciones - 1 hacer
        Leer nota_aprendices (Decimal / Float)
        suma_notas = suma_notas + nota_aprendices
      Fin Para

      promedio = suma_notas / cantidad_calificaciones
      Agregar promedio a la lista promedios
      suma_grupo = suma_grupo + promedio
    Fin Para

    Imprimir encabezado "RESULTADOS FINALES"

    // Bucle para mostrar resultados individuales
    Para i desde 0 hasta cantidad_aprendices - 1 hacer
      Imprimir nombres[i]
      Imprimir promedios[i] con 2 decimales

      Si promedios[i] >= 70 entonces
        Imprimir "Estado: Aprobado"
      Sino
        Imprimir "Estado: Reprobado"
      Fin Si

      Imprimir línea separadora
    Fin Para

    promedio_general = suma_grupo / cantidad_aprendices
    Imprimir promedio_general del grupo con 2 decimales
    Imprimir línea final decorativa

  Fin Función

  Ejecutar sistema_calificaciones()
FIN
```

---

## 3. Código Fuente

Archivo: `sistema_calificaciones.py`

```python
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
```

---

## 4. Evidencias de Ejecución

Ejecución con 3 aprendices y 3 notas por aprendiz.

**Datos de entrada**

| Aprendiz | Nota 1 | Nota 2 | Nota 3 |
|---|---|---|---|
| Ana Perez | 80 | 90 | 70 |
| Luis Gomez | 60 | 65 | 72.5 |
| Maria Lopez | 100 | 95 | 88 |

**Salida en consola (sección de resultados)**

```text
================================================================================
                             RESULTADOS FINALES
================================================================================

Aprendiz : Ana Perez
Promedio : 80.00
Estado: Aprobado
--------------------------------------------------------------------------------

Aprendiz : Luis Gomez
Promedio : 65.83
Estado: Reprobado
--------------------------------------------------------------------------------

Aprendiz : Maria Lopez
Promedio : 94.33
Estado: Aprobado
--------------------------------------------------------------------------------

Promedio general del grupo: 80.06
================================================================================
```

**Verificación manual**

- Ana Perez: (80 + 90 + 70) / 3 = 80.00, Aprobado.
- Luis Gomez: (60 + 65 + 72.5) / 3 = 65.83, Reprobado.
- Maria Lopez: (100 + 95 + 88) / 3 = 94.33, Aprobado.
- Promedio general: (80.00 + 65.83 + 94.33) / 3 = 80.06.

> Para la entrega, agrega aquí una captura de pantalla de la ejecución interactiva en tu consola.
