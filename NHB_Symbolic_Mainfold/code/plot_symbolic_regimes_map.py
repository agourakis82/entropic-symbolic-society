import numpy as np
import matplotlib.pyplot as plt
import os

# Create grid
alpha = np.linspace(0.1, 1.0, 300)
kappa = np.linspace(0.1, 1.0, 300)
A, K = np.meshgrid(alpha, kappa)

print("Alpha grid shape:", A.shape)
print("Kappa grid shape:", K.shape)

# Define symbolic regime regions (arbitrary classification for visualization)
regime_map = np.zeros_like(A)

# Define zones manually (example thresholds)
regime_map[(A > 0.6) & (K < 0.5)] = 1  # Neurotypical
regime_map[(A > 0.4) & (K > 0.6)] = 2  # Gifted
regime_map[(A > 0.3) & (A < 0.7) & (K > 0.3) & (K < 0.8)] = 3  # 2e
regime_map[(A < 0.3) | (K < 0.3)] = 4  # Collapse

print("Unique regime values:", np.unique(regime_map))

try:
    # Define colormap
    cmap = plt.colormaps.get_cmap("tab10")

    # Plot
    plt.figure(figsize=(8, 6))
    plt.contourf(A, K, regime_map, levels=[0, 1, 2, 3, 4, 5], cmap=cmap, alpha=0.75)

    # Overlay labels
    plt.text(0.75, 0.3, "Neurotypical", fontsize=10, weight='bold', color='black')
    plt.text(0.65, 0.85, "Gifted", fontsize=10, weight='bold', color='black')
    plt.text(0.45, 0.55, "2e (Oscillatory)", fontsize=10, weight='bold', color='black')
    plt.text(0.15, 0.2, "Collapse", fontsize=10, weight='bold', color='black')

    plt.xlabel(r"$\alpha$ (Anchoring)")
    plt.ylabel(r"$\kappa$ (Curvature)")
    plt.title(r"Symbolic Regime Map in the $(\alpha, \kappa)$ Space")
    plt.grid(True)

    # Save figure
    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figs'))
    os.makedirs(fig_dir, exist_ok=True)
    plt.savefig(os.path.join(fig_dir, "Fig_symbolic_regimes_map.pdf"), bbox_inches="tight")
    plt.show()
except Exception as e:
    print("Error during plot generation:", str(e))