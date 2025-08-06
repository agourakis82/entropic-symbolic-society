import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- parâmetros (mesmos da Methods) ---
η_α, η_κ, η_r = 1.0, 1.0, 1.0
K_E, K_κ = 2.0, 0.5
γ_α = 1.0
a, b = 1.5, 1.0
U, V = 1.0, 2.0
W_base, W_high = 0.2, 1.1
X, Y = 1.0, 1.0
σ = 0.1
dt, T = 1e-2, 200.0
nsteps = int(T/dt)

def φ(alpha, kappa, E, W):
    φ_a = K_E * E / (E + 0.5) - K_κ * kappa * alpha - γ_α * alpha**3
    φ_k = a * kappa - b * kappa**3 + U * alpha - V * E
    φ_r = W - X * alpha - Y * kappa
    return φ_a, φ_k, φ_r

rng = np.random.default_rng(42)
alpha = np.zeros(nsteps); kappa = np.zeros(nsteps); E = np.zeros(nsteps)
alpha[0] = 0.0; kappa[0] = 0.7; E[0] = 0.0

for i in range(nsteps-1):
    W = W_base if i*dt < 100 else W_high
    φ_a, φ_k, φ_r = φ(alpha[i], kappa[i], E[i], W)
    alpha[i+1] = alpha[i] + dt*(φ_a - η_α*alpha[i])
    kappa[i+1] = kappa[i] + dt*(φ_k - η_κ*kappa[i])
    E[i+1]     = E[i]     + dt*(φ_r - η_r*E[i]) + np.sqrt(dt)*σ*rng.standard_normal()
    if kappa[i+1] < 0: kappa[i+1] = 0
    if E[i+1] < 0: E[i+1] = 0

t = np.linspace(0, T, nsteps)
Path('NHB_Symbolic_Mainfold/figs').mkdir(parents=True, exist_ok=True)

# --- Figure 1 ---
plt.figure(figsize=(7,4))
plt.plot(t, alpha, label=r'$\alpha$')
plt.plot(t, kappa, label=r'$\kappa$')
plt.plot(t, E, label=r'$E_r$')
plt.axvline(100, ls='--', c='k')
plt.xlabel('Time (a.u.)'); plt.ylabel('State value')
plt.legend(); plt.tight_layout()
plt.savefig('NHB_Symbolic_Mainfold/figs/Fig1_collapse.png', dpi=300); plt.close()

# --- Figure 2 (bifurcation) ---
Ws = np.linspace(0.2, 1.2, 80)
alpha_ss, kappa_ss, E_ss = [], [], []
for W in Ws:
    a_tmp, k_tmp, e_tmp = 0.01, 0.7, 0.01
    for _ in range(20000):
        φ_a, φ_k, φ_r = φ(a_tmp, k_tmp, e_tmp, W)
        a_tmp += dt*(φ_a - η_α*a_tmp)
        k_tmp += dt*(φ_k - η_κ*k_tmp)
        e_tmp += dt*(φ_r - η_r*e_tmp)
    alpha_ss.append(a_tmp); kappa_ss.append(k_tmp); E_ss.append(e_tmp)

plt.figure(figsize=(7,4))
plt.plot(Ws, kappa_ss, 'o-', label=r'$\kappa^*$')
plt.plot(Ws, alpha_ss, 's-', label=r'$\alpha^*$')
plt.plot(Ws, E_ss, '^-', label=r'$E_r^*$')
plt.xlabel('Entropic drive $W$'); plt.ylabel('Steady-state value')
plt.legend(); plt.tight_layout()
plt.savefig('NHB_Symbolic_Mainfold/figs/Fig2_bifurcation.png', dpi=300); plt.close()