import numpy as np      # Para trabajar con matrices y dato snumericos 
import seaborn as sns       # Para mejorar las visualisaciónes del mapa de claro
import matplotlib.pyplot as plt     # Para gráficas
import seaborn as sns
import matplotlib.pyplot as plt

# Ejemplo de posiciones (simula posiciones detectadas)
posiciones_x = np.random.randint(0, 640, 100)
posiciones_y = np.random.randint(0, 480, 100)

# Crear el mapa de calor
plt.figure(figsize=(8, 6))
sns.kdeplot(x=posiciones_x, y=posiciones_y, cmap="Reds", fill=True)
plt.title("Mapa de Calor: Densidad de Objetos Detectados")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.show()
