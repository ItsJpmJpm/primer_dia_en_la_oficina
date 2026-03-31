# Programación Lineal para Optimizar el Reclutamiento del Ejército

# Importar Librerías Requeridas
import numpy as np
from scipy.optimize import linprog

# Definir el Problema de Programación Lineal
# Unidades: Espadachines, Arqueros, Caballería
# Costos por unidad:
# - Espadachín: 60 comida, 20 madera, 0 oro, poder 70
# - Arquero: 80 comida, 10 madera, 40 oro, poder 95
# - Caballería: 140 comida, 0 madera, 100 oro, poder 230
# Recursos: 1200 comida, 800 madera, 600 oro

# Coeficientes para la función objetivo (maximizar poder, negativo para minimización)
c = [-70, -95, -230]

# Coeficientes para las restricciones de desigualdad (Ax <= b)
A = [
    [60, 80, 140],  # comida
    [20, 10, 0],    # madera
    [0, 40, 100]    # oro
]
b = [1200, 800, 600]

# Límites para las variables (no negativas)
bounds = [(0, None), (0, None), (0, None)]

# Resolver el Problema de Optimización
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Extraer los resultados
espadachines = result.x[0]
arqueros = result.x[1]
caballeria = result.x[2]
max_poder = -result.fun

# Mostrar los Resultados
print(f"Número óptimo de Espadachines: {espadachines:.2f}")
print(f"Número óptimo de Arqueros: {arqueros:.2f}")
print(f"Número óptimo de Caballería: {caballeria:.2f}")
print(f"Poder Máximo: {max_poder:.2f}")

# Verificar restricciones
comida_usada = 60*espadachines + 80*arqueros + 140*caballeria
madera_usada = 20*espadachines + 10*arqueros
oro_usado = 40*arqueros + 100*caballeria

print("\nUso de Recursos:")
print(f"Comida: {comida_usada:.2f} / 1200")
print(f"Madera: {madera_usada:.2f} / 800")
print(f"Oro: {oro_usado:.2f} / 600")