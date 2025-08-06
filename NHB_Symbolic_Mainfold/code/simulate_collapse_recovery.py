


import numpy as np
import matplotlib.pyplot as plt
import os

# Define time axis
t = np.linspace(0, 100, 500)

# Define collapse and recovery dynamics
alpha = 0.1 + 0.5 * (1 - np.exp(-0.05 * (t - 20)))  # recovery after collapse
kappa = 0.4 + 0.1 * np.sin(0.1 * t) + 0.05 * np.random.randn(len(t))
Er = 0.8 * np.exp(-0.03 * t) + 0.05 * np.sin(0.07 * t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, alpha, label=r"$\alpha$ (Anchoring)", color="blue")
plt.plot(t, kappa, label=r"$\kappa$ (Curvature)", color="green")
plt.plot(t, Er, label=r"$E_r$ (Entropy)", color="red")
plt.title("Collapse and Recovery Simulation")
plt.xlabel("Time (t)")
plt.ylabel("Symbolic Parameters")
plt.legend()
plt.grid(True)

# Save figure
fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figs'))
os.makedirs(fig_dir, exist_ok=True)
plt.savefig(os.path.join(fig_dir, "Fig_collapse_recovery.pdf"), bbox_inches="tight")
plt.show()