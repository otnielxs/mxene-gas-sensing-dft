# Methodology

This document justifies the computational parameters and modeling choices used throughout this project. It is intended to be updated as calculations progress — sections marked *(TBD)* will be filled in with actual data as results become available.

---

## 1. Computational Parameters (Quantum ESPRESSO)

### 1.1 Energy Cutoff (ecutwfc / ecutrho)

Convergence testing was performed on the pristine Ti₂CO₂ monolayer (without adsorbed gas molecules) to keep the test computationally light while still representative of the production system.

**Procedure:**
- Total energy computed at increasing cutoff values (e.g., 30, 35, 40, 45, 50 Ry), keeping all other parameters fixed
- Convergence threshold: total energy difference between successive steps < 1–5 meV/atom
- Charge density cutoff (`ecutrho`) set according to the pseudopotential type used (typically 8× `ecutwfc` for PAW)

**Result:** *Ti₂CO₂ converged in ecutwfc 60 Ry, ecutrho 480 Ry*. only for first approach, i use 40 and 320. you can use higher if your resources is required 


Pseudopotential used: *(type: Projector Augmented Wave)*

### 1.2 K-point Sampling

**Procedure:**
- In-plane (x, y) k-point grid tested from coarse (4×4×1) to finer (6×6×1, 8×8×1) on the pristine monolayer. but since i make 2 times in x direction, i use (2x4x1 for relax, 3x6x1 for scf, and 4x8x1 for nscf) 
- Out-of-plane (z) k-point fixed at 1, since the slab has no periodicity along the vacuum direction
- Monkhorst-Pack shifted grid used (rather than Γ-point only), appropriate for the unit cell size used here

For adsorption calculations using a larger supercell (to avoid spurious interaction between periodic images of the adsorbed molecule), the k-point grid was scaled down proportionally relative to the unit cell.

### 1.3 Smearing and SCF Settings

- Smearing scheme: Marzari-Vanderbilt (cold smearing), degauss = *(0.02 Ry)* — appropriate given the semi-metallic character of Ti₂CO₂
- Mixing beta: *(default)*

### 1.4 van Der Waals Correction

- For capturing vdW interactions, **DFT-D3** implemented on **vdw_corr**
---

## 2. Slab Construction

- Unit cell / supercell size: *(multiplicity in x direction 2 times)*
- Vacuum layer thickness: *(5 Å)* — chosen to minimize spurious interaction between periodic images along the surface normal while avoiding unnecessary computational cost from excess vacuum **for better result suggested > 15 Å*
- Termination group: =O (oxygen-terminated Ti₂CO₂, as commonly studied in the MXene gas-sensing literature)
- Number of gas molecules per supercell: 1 (isolated adsorption, low-coverage regime)
- Molecule initial placement: *(on top, oxygen site)*

---

## 3. Cluster Model Construction (ORCA)

Because periodic DFT captures surface-averaged electronic effects but is less suited to resolving local bonding topology in detail, a complementary cluster model was built for each adsorption case.

- **Cluster extraction:** the cluster was cut from the relaxed periodic adsorption geometry, centered on the adsorption site, including the immediate coordination environment of the gas molecule
- **Cluster size:** *(1 unit cell)*
- **Geometry:** the cluster geometry was kept fixed from the periodic-relaxed structure for single-point analysis, or re-optimized

---

## 4. Method Choice Justification (ORCA)

- **Functional:** *(B3LYP)*
- **Basis set strategy:** geometry optimization performed with a smaller basis set (def2-SVP) first; single-point energy refinement at the optimized geometry performed with a larger basis set (def2-TZVP), balancing accuracy against the computational budget available (local laptop, RTX 3050 6GB / CPU-bound ORCA run)
- **Dispersion correction:** D3(BJ) included, since the interactions of interest (particularly for CO₂ and H₂S) are expected to be dominated or significantly influenced by van der Waals forces rather than strong covalent bonding
- **RI approximation:** RIJCOSX used to reduce computational cost without significant loss of accuracy, appropriate given local hardware constraints

---

## 5. Post-Processing Methods

### 5.1 Quantum ESPRESSO (`pp.x and projwfc.x`)
- **Charge density difference (Δρ):** Δρ = ρ(slab+molecule) − ρ(slab) − ρ(molecule), computed on the relaxed adsorption geometry, holding atomic positions fixed across the three calculations
- **Planar-averaged electrostatic potential:** used to estimate the work function shift upon adsorption, a key indicator for sensing sensitivity
- **Projected density of states (PDOS):** used to identify which orbitals (Ti-d, O-p, N-s, H-s, C-p, S-p) contribute to the interaction near the Fermi level

### 5.2 Multiwfn
- **NCI (Non-Covalent Interaction) plot:** used to visualize and classify the interaction type (van der Waals, weak hydrogen bonding, steric repulsion) at the adsorption site
- **ELF (Electron Localization Function):** used to characterize electron localization and bonding character (covalent vs. non-bonded)
- **Bader charge analysis:** used to quantify charge transfer at the cluster level, for cross-validation against the periodic charge-density-difference result

---

## 6. Limitations and Cross-Method Considerations

- Periodic DFT captures collective electronic response of the full 2D material (e.g., work function, band-level shifts) but the finite k-point/cutoff choices represent a compromise between accuracy and the computational resources available for this project
- Discrepancies between the two methods' charge-transfer estimates, if found, are expected primarily from these structural and methodological differences rather than from calculation error — this will be discussed explicitly once both result sets are available *(TBD — fill in once comparison is complete)*
- Try some multiplicity factor, especially for Ti₂CO₂ and NO₂ for founding ground state level (ORCA) 
- Try realistic cluster with adding some Hydrogen atoms on surface (ORCA)
---

## Revision Log

| Date | Change |
|---|---|
| *18/09/2026* | Initial draft|
| *19/09/2026* | QE running |
| *20/09/2026* | ORCA running |
| *21/09/2026* | Write results |
