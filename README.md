# Gas Molecule Adsorption on MXene Ti₂CO₂ Monolayer: A Multi-Method DFT Bonding Analysis

A computational study of gas molecule adsorption (NH₃, CO₂, H₂S) on Ti₂CO₂ MXene monolayer, using complementary **periodic DFT (Quantum ESPRESSO)** and **cluster model (ORCA + Multiwfn)** approaches to evaluate the potential of Ti₂CO₂ as a gas-sensing material.

## Motivation

Ti₂CO₂ MXene has drawn significant attention as a candidate gas-sensor material because its surface termination group (=O) is sensitive to small gas molecule adsorption, which manifests as changes in work function and local charge distribution. This project explores that interaction from two complementary perspectives:

- **Periodic DFT (QE)** — captures the electronic response of the material as a full slab (band structure, work function, surface-scale charge transfer)
- **Cluster model (ORCA + Multiwfn)** — captures the local bonding character at the adsorption site in finer detail (interaction type, bonding topology)

The periodic-DFT methodology in this project builds on prior thesis research on the Ti₂CO₂/MoS₂ heterostructure for aluminum-ion battery applications.

## Research Questions

1. What is the adsorption character (physisorption vs. chemisorption) of each gas molecule on the Ti₂CO₂ surface?
2. How large is the work function change upon adsorption, and is it significant enough for sensing applications?
3. Is the charge-transfer trend from the periodic model (QE) consistent with the cluster model (ORCA/Multiwfn)?

## Methodology

### 1. Periodic DFT (Quantum ESPRESSO)
- Ti₂CO₂ monolayer slab with a vacuum layer, optimized prior to gas molecule adsorption
- Computational parameters (cutoff energy, k-points) determined via convergence testing on the pristine monolayer — see [`docs/methodology.md`](docs/methodology.md)
- Adsorption energy calculation: E_ads = E_(slab+molecule) − E_slab − E_molecule
- Post-processing with `pp.x`:
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
| NH₃    | *(to be filled in once results are available)* |
| CO₂    | *(to be filled in once results are available)* |
| H₂S    | *(to be filled in once results are available)* |

## Key Results

*(This section will be filled in once calculations are complete — placeholder for key figures)*

- Adsorption energy for each molecule: `[table/chart]`
- Charge density difference maps: `[figure]`
- Work function changes: `[chart]`
- NCI plot per molecule: `[figure]`

## Repository Structure

```
mxene-gas-sensing-dft/
├── README.md
├── qe/
│   ├── inputs/         # scf, relax, pp.x inputs per gas molecule
│   └── scripts/        # pp.x output parsing, Δρ & potential plotting
├── orca-multiwfn/
│   ├── inputs/         # Cluster model ORCA inputs
│   └── scripts/        # Multiwfn input automation, NCI/ELF plotting
├── figures/             # Charge density, NCI plots, band alignment
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
# QE calculations (run on HPC cluster)
cd qe/inputs/
pw.x < scf_ti2co2_nh3.in > scf_ti2co2_nh3.out

# Post-processing
pp.x < pp_chdens.in > pp_chdens.out
python ../scripts/plot_charge_density.py

# Cluster model with ORCA (run locally)
cd orca-multiwfn/inputs/
orca cluster_nh3.inp > cluster_nh3.out

# Multiwfn analysis
Multiwfn cluster_nh3.molden < ../scripts/nci_settings.txt
```

## Project Status

🚧 *Work in progress* 

