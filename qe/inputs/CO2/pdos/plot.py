import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

EF_MXENE  =  # fermi level
EF_MXENE+GAS   =  # fermi level

emin = -4
emax = 4

def load_pdos(filename, EF):
    data = np.loadtxt(filename)
    E = data[:, 0] - EF
    DOS = data[:, 1]
    mask = (E >= emin) & (E <= emax)
    return E[mask], DOS[mask]

E1, ATOM_pristine   = load_pdos("wfc file", EF_MXENE) # select which ATOM and orbital that want to projected
E2, ATOM_pristine  = load_pdos("wfc file", EF_MXENE) # select which ATOM and orbital that want to projected
E3, ATOM_ads     = load_pdos("wfc file", EF_MXENE+GAS) # select which ATOM and orbital that want to projected
E4, ATOM_ads    = load_pdos("wfc file", EF_MXENE+GAS) # select which ATOM and orbital that want to projected

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.linewidth": 1.2,
    "xtick.major.width": 1,
    "ytick.major.width": 1
})

fig = plt.figure(figsize=(6, 6))
gs = gridspec.GridSpec(4, 1, hspace=0.06)
axes = [fig.add_subplot(gs[i]) for i in range(4)]

def plot_panel(ax, E, DOS, color):
    ax.plot(E, DOS, color=color, linewidth=1.3)
    ax.fill_between(E, DOS, 0, color=color, alpha=0.3)
    ax.axvline(0, linestyle='--', color='black', linewidth=1)
    ax.set_xlim(emin, emax)
    ax.set_ylim(bottom=0)

plot_panel(axes[0], E1, ATOM_pristine,  'RGB') # choose colour RGB
plot_panel(axes[1], E2, ATOM_pristine, 'RGB') # choose colour RGB
plot_panel(axes[2], E3, ATOM_ads,    'RGB') # choose colour RGB
plot_panel(axes[3], E4, ATOM_ads,   'RGB') # choose colour RGB

axes[0].text(0.97, 0.88, "ATOM-ORBITAL", transform=axes[0].transAxes, # ATOM-ORBITAL, e.g H-1s
             ha='right', va='top')

axes[1].text(0.97, 0.88, "ATOM-ORBITAL", transform=axes[1].transAxes, # ATOM-ORBITAL, e.g H-1s
             ha='right', va='top')

axes[2].text(0.97, 0.88, "ATOM-ORBITAL", transform=axes[2].transAxes, # ATOM-ORBITAL, e.g H-1s
             ha='right', va='top')

axes[3].text(0.97, 0.88, "ATOM-ORBITAL", transform=axes[3].transAxes, # ATOM-ORBITAL, e.g H-1s
             ha='right', va='top')

fig.supylabel("DOS (states/eV)", x=0.03)
fig.supxlabel("Energy (eV)")

for ax in axes[:-1]:
    ax.tick_params(labelbottom=False)

plt.subplots_adjust(left=0.14, right=0.98,
                    top=0.98, bottom=0.10)

plt.show()
