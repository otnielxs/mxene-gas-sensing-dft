import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

colors = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]  # blue → green → red
nci_cmap = LinearSegmentedColormap.from_list('nci', colors, N=256)

systems = {
    'co2': r'$\mathrm{CO_2}$',
    'h2s': r'$\mathrm{H_2S}$',
    'nh3': r'$\mathrm{NH_3}$',
    'no2': r'$\mathrm{NO_2}$',
}

fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
axes = axes.flatten()

for i, (sys, label) in enumerate(systems.items()):
    filename = f'{sys}_scatter.txt'
    try:
        data = np.loadtxt(filename)
        x = data[:, 3]
        y = data[:, 4]

        ax = axes[i]
        sc = ax.scatter(
            x, y, c=x, cmap=nci_cmap, s=1.0, vmin=-0.05, vmax=0.05, alpha=0.6
        )
        ax.set_title(f'$\\mathrm{{Ti_2CO_2}}$ + {label}', fontsize=12)
        ax.set_xlim(-0.05, 0.05)
        ax.set_ylim(0, 2.0)
        ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
        ax.grid(True, linestyle=':', alpha=0.6)

    except OSError:
        print(f'{filename} not found.')
for ax in axes:
    ax.grid(False)


fig.text(0.5, 0.02, r'$\mathrm{sign}(\lambda_2)\rho$ (a.u.)', ha='center', fontsize=14)
fig.text(0.02, 0.5, 'RDG (a.u.)', va='center', rotation='vertical', fontsize=14)

plt.tight_layout(rect=[0.03, 0.03, 1, 1])
plt.savefig('rdg-combined.png', dpi=300)
plt.show()
