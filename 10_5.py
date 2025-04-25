import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**3 - x - 2
def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    updates = []
    if f(a) * f(b) > 0:
        raise ValueError("Function values at the endpoints must have opposite signs.")
    for _ in range(max_iter):
        m = (a + b) / 2
        updates.append(m)
        if abs(f(m)) < tol:
            break
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return np.array(updates)
np.random.seed(0)
a = np.random.uniform(-5, 5)
b = np.random.uniform(-5, 5)
while f(a) * f(b) > 0:
    a = np.random.uniform(-5, 5)
    b = np.random.uniform(-5, 5)
updates = bisection_method(f, a, b)
x = np.linspace(-3, 3, 400)
y = f(x)
plt.plot(x, y, label='f(x) = x^3 - x - 2', color='b')
plt.axhline(0, color='k',linewidth=1)
plt.title('Bisection Method Root Finding Process')
plt.scatter(updates, f(updates), color='r', zorder=5, label='Midpoints')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()