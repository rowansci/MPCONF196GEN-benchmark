# mpconf196-gen-benchmark
A conformer generation benchmark created from the MPCONF196 benchmark energy dataset [1]. This evaluates a method's ability to generate conformers of macrocycles, a difficult task for molecular conformer generation.

Reference conformers were generated with CREST [2] iMTD-GC [3] using GFN2-xTB [3] and conformer energies were computed using Egret-1 [4] neural network potential.

# Usage
`SMILES.txt` contains the number of rotateable bonds, canonical SMILES strings and identifier for each molecule. Each `molecules/{molecule_id}/` directory contains a `crest_conformers_egret.extxyz` file with conformers and energies for each molecule.

# Creating the Benchmark

All packages necessary for making this benchmark can be installed by creating a conda envrionment from `env.yml`. We ran CREST on each `data/{molecule_id}.xyz` file, outputs and conformers can be found in `molecules/{molecule_id}/crest.out` and `molecules/{molecule_id}/crest_confromers.xyz` files respectively. The Egret-1 checkpoint and scripts used to calculate conformer energies and create the `SMILES.txt` file can be found in the `tools/` directory. SMILES for each molecule were generated from the `data/{molecule_id}.xyz` files on rowansci.com, except for `data/YIVNOG_I.xyz` which we made by hand.
