


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define time axis
t = np.linspace(0, 100, 500)

# Define symbolic parameters for each cognitive profile
def gamma_neurotypical(t):
    alpha = 0.9 * np.ones_like(t)
    kappa = 0.5 + 0.1 * np.sin(0.05 * t)
    Er = 0.3 + 0.05 * np.sin(0.03 * t)
    return alpha, kappa, Er

def gamma_gifted(t):
    alpha = 0.6 + 0.1 * np.cos(0.07 * t)
    kappa = 0.8 + 0.15 * np.sin(0.09 * t)
    Er = 0.6 + 0.2 * np.sin(0.04 * t)
    return alpha, kappa, Er

def gamma_2e(t):
    alpha = 0.5 + 0.3 * np.sin(0.15 * t)
    kappa = 0.4 + 0.4 * np.sin(0.11 * t)
    Er = 0.7 + 0.3 * np.cos(0.12 * t)
    return alpha, kappa, Er

def gamma_collapse(t):
    alpha = 0.8 * np.exp(-0.03 * t)
    kappa = 0.5 + 0.1 * np.random.randn(len(t))
    Er = 0.4 + 0.01 * t + 0.05 * np.sin(0.1 * t)
    return alpha, kappa, Er

# Generate all profiles
profiles = {
    "Neurotypical": gamma_neurotypical(t),
    "Gifted": gamma_gifted(t),
    "2e": gamma_2e(t),
    "Collapse": gamma_collapse(t),
}

# Plotting
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

for idx, (label, (alpha, kappa, Er)) in enumerate(profiles.items()):
    axs[idx].plot(t, alpha, label=r"$\alpha$", color="blue")
    axs[idx].plot(t, kappa, label=r"$\kappa$", color="green")
    axs[idx].plot(t, Er, label=r"$E_r$", color="red")
    axs[idx].set_title(f"{label} Profile")
    axs[idx].legend(loc="upper right")
    axs[idx].grid(True)

axs[-1].set_xlabel("Time (t)")
plt.tight_layout()
plt.savefig("../figs/Fig_gamma_profiles.pdf", bbox_inches="tight")
plt.show()