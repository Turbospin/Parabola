a = float(input("Podaj a: ")) 
b = float(input("Podaj b: ")) 
c = float(input("Podaj c: ")) 
import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(-10, 10, 400) 
y = a*x**2 + b*x + c 
plt.plot(x, y) 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Wykres paraboli") 
plt.grid(True) 
plt.show() 
plt.title(f"Wykres paraboli: y = {a}x^2 + {b}x + {c}") 
