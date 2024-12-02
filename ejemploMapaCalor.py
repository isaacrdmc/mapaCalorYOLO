import numpy as np      # Para trabajar con matrices y dato snumericos 
import seaborn as sns       # Para mejorar las visualisaciónes del mapa de claro
import matplotlib.pyplot as plt     # Para gráficas
# ? pip install numpy matplotlib seaborn        # Comando de la instalación


# Generando datos ficticios
# ? Creamos una matriz 10x10 de valores aleatorios para las variables
np.random.seed(0)  # Para reproducibilidad
temperatura = np.random.rand(10, 10) * 40  # Temperaturas entre 0 y 40 grados
humedad = np.random.rand(10, 10) * 100     # Humedad entre 0 y 100%

# ? Usamos seaborn para crear el mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(temperatura + humedad, annot=True, fmt=".1f", cmap="coolwarm", cbar=True)

# ? Personalización del gráfico
plt.title("Mapa de Calor: Temperatura + Humedad")
plt.xlabel("Índice X")
plt.ylabel("Índice Y")

# ^ Mostrar el gráfico
plt.show()
