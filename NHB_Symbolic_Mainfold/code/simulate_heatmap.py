


import numpy as np
import matplotlib.pyplot as plt
import os

# Define parameter space
alpha_vals = np.linspace(0.1, 1.0, 100)
kappa_vals = np.linspace(0.1, 1.0, 100)
alpha_grid, kappa_grid = np.meshgrid(alpha_vals, kappa_vals)

# Fixed entropy
Er = 0.5

# Compute symbolic density function (e.g., symbolic coherence index)
# This is a placeholder: update the function as needed for your model
D = alpha_grid * kappa_grid * np.exp(-Er)

# Plot heatmap
plt.figure(figsize=(8, 6))
plt.imshow(D, origin="lower", extent=[alpha_vals.min(), alpha_vals.max(), kappa_vals.min(), kappa_vals.max()],
           aspect="auto", cmap="plasma")
plt.colorbar(label="Symbolic Density (D)")
plt.xlabel(r"$\alpha$ (Anchoring)")
plt.ylabel(r"$\kappa$ (Curvature)")
plt.title("Symbolic Manifold Heatmap ($E_r$ fixed)")

# Save figure
fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figs'))
os.makedirs(fig_dir, exist_ok=True)
plt.savefig(os.path.join(fig_dir, "Fig_symbolic_heatmap.pdf"), bbox_inches="tight")
plt.show()