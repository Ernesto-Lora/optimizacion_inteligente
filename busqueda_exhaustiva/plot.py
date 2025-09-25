import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango, excluyendo el 0
x = np.linspace(-10, 10, 5000)
x = x[x != 0]  # quitamos el cero para evitar la división

# Definimos la función
f = np.real(np.power(x, 2)) + 54/x

# Graficamos
plt.figure(figsize=(8,6))
plt.plot(x, f, label=r"$f(x) = x^2 + \frac{54}{x}$", color="blue")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="red", linewidth=0.8, linestyle="--", label="x=0 (discontinuity)")

plt.ylim(-500, 500)  # para que no explote la escala
plt.legend()
#plt.title("Gráfica de $f(x) = x^2 + 54/x$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

# Guardar en PDF
plt.savefig("grafica_funcion.pdf")
plt.show()
