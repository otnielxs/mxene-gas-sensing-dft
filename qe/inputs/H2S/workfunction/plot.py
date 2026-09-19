import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("avg.dat")
z = data[:, 0]        # posisi z (Bohr)
V_planar = data[:, 1]   # V_p(z)
V_macro = data[:, 2]    # V_m(z)

E_F =           # Fermi level (eV)

V_vac = np.max(V_planar)
Phi = V_vac - E_F     # Work function (\Phi)

z_arrow =   # point V_p(z)

plt.figure(figsize=(7, 5))
plt.plot(z, V_planar, color='purple', label=r'$V_p(z)$ - Planar')
plt.plot(z, V_macro, color='teal', label=r'$V_m(z)$ - Macroscopic')

plt.axhline(E_F, color='blue', linestyle='--', linewidth=1.2, label=r'$E_F$ - Fermi')

plt.annotate(
    '',
    xy=(z_arrow, V_vac),
    xytext=(z_arrow, E_F),
    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5)
)

plt.text(
    z_arrow + 0.5, (E_F + V_vac) / 2,
    f'$\Phi \\sim {Phi:.2f}$ eV',
    va='center', ha='left', fontsize=10, color='black'
)

plt.xlabel("Position z (Bohr)")
plt.ylabel("Energy (eV)")
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.show()
