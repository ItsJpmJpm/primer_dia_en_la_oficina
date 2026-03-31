# Programación Lineal para Optimizar el Reclutamiento del Ejército

# Definir el Problema de Programación Lineal
# Unidades: Espadachines, Arqueros, Caballería
# Costos por unidad:
# - Espadachín: 60 comida, 20 madera, 0 oro, poder 70
# - Arquero: 80 comida, 10 madera, 40 oro, poder 95
# - Caballería: 140 comida, 0 madera, 100 oro, poder 230
# Recursos: 1200 comida, 800 madera, 600 oro

# Recursos disponibles
comida_total = 1200
madera_total = 800
oro_total = 600

# Definir costos y poder de cada unidad
# [comida, madera, oro, poder]
espadachin_costo = [60, 20, 0, 70]
arquero_costo = [80, 10, 40, 95]
caballeria_costo = [140, 0, 100, 230]

# Búsqueda exhaustiva para encontrar la solución óptima
mejor_poder = 0
mejor_solucion = {}

# Límites máximos aproximados para la búsqueda
max_espadachines = comida_total // espadachin_costo[0] + 1
max_arqueros = comida_total // arquero_costo[0] + 1
max_caballeria = comida_total // caballeria_costo[0] + 1

# Búsqueda exhaustiva
for espadachines in range(max_espadachines):
    for arqueros in range(max_arqueros):
        for caballeria in range(max_caballeria):
            # Calcular consumo de recursos
            comida_usada = espadachines * espadachin_costo[0] + arqueros * arquero_costo[0] + caballeria * caballeria_costo[0]
            madera_usada = espadachines * espadachin_costo[1] + arqueros * arquero_costo[1] + caballeria * caballeria_costo[1]
            oro_usado = espadachines * espadachin_costo[2] + arqueros * arquero_costo[2] + caballeria * caballeria_costo[2]
            
            # Verificar que no exceda los recursos disponibles
            if comida_usada <= comida_total and madera_usada <= madera_total and oro_usado <= oro_total:
                # Calcular poder total
                poder_total = espadachines * espadachin_costo[3] + arqueros * arquero_costo[3] + caballeria * caballeria_costo[3]
                
                # Actualizar mejor solución si es mejor
                if poder_total > mejor_poder:
                    mejor_poder = poder_total
                    mejor_solucion = {
                        'espadachines': espadachines,
                        'arqueros': arqueros,
                        'caballeria': caballeria,
                        'comida_usada': comida_usada,
                        'madera_usada': madera_usada,
                        'oro_usado': oro_usado
                    }

# Mostrar los Resultados
print("=" * 50)
print("SOLUCIÓN ÓPTIMA DE RECLUTAMIENTO DEL EJÉRCITO")
print("=" * 50)
print(f"\nNúmero óptimo de Espadachines: {mejor_solucion['espadachines']}")
print(f"Número óptimo de Arqueros: {mejor_solucion['arqueros']}")
print(f"Número óptimo de Caballería: {mejor_solucion['caballeria']}")
print(f"\nPoder Máximo: {mejor_poder}")

# Verificar restricciones y usar de recursos
print("\nUso de Recursos:")
print(f"Comida: {mejor_solucion['comida_usada']} / {comida_total}")
print(f"Madera: {mejor_solucion['madera_usada']} / {madera_total}")
print(f"Oro: {mejor_solucion['oro_usado']} / {oro_total}")