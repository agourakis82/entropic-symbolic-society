import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Time vector
t = np.linspace(0, 100, 500)

# Define synthetic trajectory γ(t)
alpha = 0.6 + 0.2 * np.sin(0.05 * t)                # Anchoring
kappa = 0.4 + 0.3 * np.cos(0.03 * t + 1.2)           # Curvature
Er = 0.5 + 0.1 * np.sin(0.07 * t + 0.8)              # Entropy rate

# Create 3D figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot trajectory
ax.plot(alpha, kappa, Er, label=r'$\gamma(t)$ trajectory', color='purple', linewidth=2)

# Highlight start and end
ax.scatter(alpha[0], kappa[0], Er[0], color='green', s=50, label="Start")
ax.scatter(alpha[-1], kappa[-1], Er[-1], color='red', s=50, label="End")

# Axis labels
ax.set_xlabel(r'$\alpha$ (Anchoring)')
ax.set_ylabel(r'$\kappa$ (Curvature)')
ax.set_zlabel(r'$E_r$ (Entropy Rate)')
ax.set_title(r'3D Symbolic Trajectory $\gamma(t)$ in $(\alpha, \kappa, E_r)$ space')
ax.legend()

# Save figure
fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figs'))
os.makedirs(fig_dir, exist_ok=True)
fig_path = os.path.join(fig_dir, 'Fig_trajectory_3D.pdf')
plt.savefig(fig_path, bbox_inches='tight')
plt.show()