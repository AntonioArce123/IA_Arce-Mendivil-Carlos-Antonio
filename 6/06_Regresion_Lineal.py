import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)


modelo = LinearRegression()
modelo.fit(x, y)

y_pred = modelo.predict(x)

print("Coeficiente (pendiente):", modelo.coef_[0][0])
print("Intersección (bias):", modelo.intercept_[0])
print("R^2 Score:", r2_score(y, y_pred))

# Gráfico creeado a partir de los datos y la línea de regresión (con gpt)
plt.scatter(x, y, color="blue", label="Datos")
plt.plot(x, y_pred, color="red", label="Línea de Regresión")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Regresión Lineal")
plt.legend()
plt.grid(True)
plt.show()
