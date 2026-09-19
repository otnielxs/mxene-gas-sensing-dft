# Gas Molecule Adsorption on MXene Ti₂CO₂ Monolayer: A Multi-Method DFT Bonding Analysis

A computational study of gas molecule adsorption (NH₃, CO₂, NO₂, H₂S) on Ti₂CO₂ MXene monolayer, using complementary **periodic DFT (Quantum ESPRESSO)** and **cluster model (ORCA + Multiwfn)** approaches to evaluate the potential of Ti₂CO₂ as a gas-sensing material.

## Motivation

Ti₂CO₂ MXene has drawn significant attention as a candidate gas-sensor material because its surface termination group (=O) is sensitive to small gas molecule adsorption, which manifests as changes in work function and local charge distribution. This project explores that interaction from two complementary perspectives:

- **Periodic DFT (QE)** — captures the electronic response of the material as a full slab (band structure, work function, surface-scale charge transfer)
- **Cluster model (ORCA + Multiwfn)** — captures the local bonding character at the adsorption site in finer detail (interaction type, bonding topology)

The periodic-DFT methodology in this project builds on prior thesis research on the Ti₂CO₂/MoS₂ heterostructure for aluminum-ion battery applications.

**Status: adsorption energies for all four gas molecules are now favorable (exothermic), giving initial support to Ti₂CO₂ as a gas-sensitive surface for NH₃, CO₂, NO₂, and H₂S.**

## Research Questions

1. What is the adsorption character (physisorption vs. chemisorption) of each gas molecule on the Ti₂CO₂ surface?
2. How large is the work function change upon adsorption, and is it significant enough for sensing applications?
3. Is the charge-transfer trend from the periodic model (QE) consistent with the cluster model (ORCA/Multiwfn)?

## Methodology

### 1. Periodic DFT (Quantum ESPRESSO)
- Ti₂CO₂ monolayer slab with a vacuum layer, optimized prior to gas molecule adsorption
- Computational parameters (cutoff energy, k-points) determined via convergence testing on the pristine monolayer — see [`docs/methodology.md`](docs/methodology.md)
- Adsorption energy calculation: E_ads = E_(slab+molecule) − E_slab − E_molecule
- Post-processing with `pp.x` and `projwfc.x`:
  - Charge density difference (Δρ)
  - Planar-averaged electrostatic potential (work function shift)
  - Projected density of states (PDOS)

### 2. Cluster Model (ORCA + Multiwfn)
- A representative cluster is cut from the adsorption site of the periodic structure
- Geometry optimization and single-point energy with DFT-D3(BJ) to capture dispersion contributions relevant to physisorption
- Multiwfn analysis:
  - NCI (Non-Covalent Interaction) plot
  - ELF (Electron Localization Function)
  - Bader charge analysis

### 3. Cross-Method Synthesis
Comparison of charge transfer and bonding character between the two approaches to evaluate consistency and the limitations of each method.

## Gas Molecules Studied

| Molecule | Rationale |
|---|---|
| NH₃  | Common indoor/industrial air pollutant; tests sensitivity to a simple lone-pair electron donor |
| CO₂  | Ubiquitous, chemically stable, linear nonpolar molecule; tests sensitivity to a weakly-interacting closed-shell gas |
| NO₂  | Toxic combustion byproduct with open-shell (radical) character; tests sensitivity to a reactive, unpaired-electron species |
| H₂S  | Toxic, corrosive industrial/biological gas; tests sensitivity to a polarizable, sulfur-containing molecule |

## Key Results

### Adsorption Energy (Quantum ESPRESSO)

| Molecule | E_ads (eV) |
|---|---|
| NH₃ | −1.556 |
| CO₂ | −1.590 |
| NO₂ | −1.542 |
| H₂S | **−1.859** |

All four molecules show **favorable (exothermic) adsorption**. H₂S shows the strongest binding, consistently across every indicator used in this study (energetics, Löwdin charge, PDOS hybridization, and work function shift — see `docs/methodology.md` for the full cross-indicator discussion). NH₃, CO₂, and NO₂ show comparable adsorption energies to one another (within ~0.05 eV), though their charge-transfer character differs (see below) — this is discussed further in the full analysis rather than treated as a strict potency ranking.

### Löwdin Charge Transfer

- **H₂S** shows by far the largest charge redistribution (≈0.36 e transferred from the molecule to the slab, concentrated on the S atom) — consistent with a more ionic/charge-transfer-dominated interaction
- **NH₃** shows a moderate, clearly non-negligible transfer on the N atom
- **CO₂ and NO₂** show comparatively small net charge transfer despite their substantial adsorption energies — suggesting their binding is driven more by orbital hybridization (covalent-like sharing) than by net charge transfer

### Charge Density Difference & PDOS

Charge density difference maps and PDOS (before vs. after adsorption) support the picture above: H₂S and NH₃ show visibly larger, more localized redistribution and new hybridized states near the Fermi level after adsorption, while CO₂ and NO₂ show sharper, more weakly-perturbed states consistent with their smaller net charge transfer. *(Figures to be added to `figures/`.)*

### Work Function Shift

| System | ΔΦ (eV) |
|---|---|
| Pristine | ~0.18 (baseline) |
| + NH₃  | −0.39 |
| + CO₂  | −0.67 |
| + NO₂  | −0.60 |
| + H₂S  | **−0.84** |

Shifts range from 0.39–0.84 eV, well within the range typically considered significant for chemiresistive/work-function-based gas sensing (experimental resolution is commonly on the order of tens of meV). The magnitude ordering (H₂S > CO₂ > NO₂ > NH₃) is consistent with the adsorption energy ordering.

### Adsorption Character (Q1 — preliminary)

Based on the magnitude of E_ads (1.5–1.9 eV, larger than typical physisorption) combined with the charge-transfer pattern above, the preliminary picture is that **all four molecules interact strongly with the Ti₂CO₂ surface**, but through different mechanisms:
- **H₂S**: strong interaction with substantial net charge transfer — more ionic/charge-transfer character
- **NH₃, CO₂, NO₂**: strong interaction with minimal net charge transfer — more consistent with covalent-like orbital hybridization

This nuance will be cross-checked against the ORCA/Multiwfn cluster model (Bader charge, NCI, ELF) once that stage is complete.

### Cross-Method Consistency (Q3 — pending)

Not yet evaluated — cluster models for the ORCA/Multiwfn stage are in progress. The key check will be whether Bader charge analysis also ranks H₂S as the largest charge-transfer case, consistent with the Löwdin charge result from QE.

## Repository Structure

```
mxene-gas-sensing-dft/
├── README.md
├── qe/
│   ├── inputs/         # relax, scf, nscf, pp.x inputs per gas molecule
│   └── scripts/        # pp.x output parsing, Δρ & potential plotting
├── orca-multiwfn/
│   ├── inputs/         # Cluster model ORCA inputs
│   └── scripts/        # Multiwfn input automation, NCI/ELF plotting
├── figures/             # Charge density, PDOS, workfunction, NCI plots
└── docs/
    └── methodology.md   # Cluster model justification & DFT parameters
```

## Software Used

- [Quantum ESPRESSO](https://www.quantum-espresso.org/) — periodic DFT calculations
- [ORCA](https://orcaforum.kofo.mpg.de/) — cluster model quantum chemistry
- [Multiwfn](http://sobereva.com/multiwfn/) — wavefunction analysis (NCI, ELF, Bader charge)
- Python (NumPy, Matplotlib) — parsing & visualization

## Reproducing the Results

```bash
# QE calculations
cd qe/inputs/
pw.x < s_nh3.in > s_nh3.out

# Post-processing
pp.x < a_nh3.in > a_nh3.out
python3 plot.py

# Cluster model with ORCA (run locally)
cd orca-multiwfn/inputs/
orca nh3.inp > nh3.out

# Multiwfn analysis
Multiwfn cluster_nh3.molden < ../scripts/nci_settings.txt
```

## Project Status

🚧 *Work in progress*
- ✅ QE adsorption energies, Löwdin charges, charge density difference, PDOS, and work function — complete for all four molecules
- ⏳ ORCA cluster model construction and Multiwfn analysis (NCI, ELF, Bader charge) — in progress
- ⏳ Cross-method synthesis (Q3) — pending ORCA/Multiwfn results

