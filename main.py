import numpy as np

# set up a grid from -1 to 1 with 100 points:
N = 100 # number of points
L = 5 # box size
x = np.linspace(-L, L, N)
dx = 2*L/(N - 1)

# constants:
Omega = 1 # trap frequency, set to 1 for now

# define operators:
v = Omega**2/2 * x**2 # one-body harmonic oscillator potential

# matrix representations in DVR:
V = np.diag(v) # one-body harmonic oscillator potential

T = np.zeros((N, N), dtype=float) # one-body kinetic energy
for alpha in range(N):
    for beta in range(N):
        if alpha == beta:
            T[alpha, beta] = np.pi**2 / (6 * dx**2)
        else:
            T[alpha, beta] = (-1)**(alpha - beta) / (dx**2 * (alpha - beta)**2)

H = T + V

vals, vecs = np.linalg.eigh(H)

print(vals)

