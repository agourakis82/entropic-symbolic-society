import numpy as np
import matplotlib.pyplot as plt
import os

# Time axis
t = np.linspace(0, 100, 500)

# Fixed parameters
alpha = np.full_like(t, 0.6)
Er = np.full_like(t, 0.4)

# Bifurcating curvature
kappa = 0.3 + 0.0015 * (t**2) * np.sin(0.1 * t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, alpha, label=r"$\alpha$ (Anchoring)", color="blue", linestyle="--")
plt.plot(t, kappa, label=r"$\kappa$ (Curvature)", color="green")
plt.plot(t, Er, label=r"$E_r$ (Entropy)", color="red", linestyle=":")
plt.axvline(x=60, color='black', linestyle=':', label="Bifurcation Threshold")
plt.title("Bifurcation Simulation via $\kappa(t)$")
plt.xlabel("Time (t)")
plt.ylabel("Symbolic Parameters")
plt.legend()
plt.grid(True)

# Save figure
fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figs'))
os.makedirs(fig_dir, exist_ok=True)
plt.savefig(os.path.join(fig_dir, "Fig_kappa_bifurcation.pdf"), bbox_inches="tight")
plt.show()