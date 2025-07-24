import os
import numpy as np
import ase.io
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


SMILES = {
        "CAMVES_I": "C[C@@H]1NC(=O)[C@H](C)NC(=O)[C@@H]2CCCN2C(=O)[C@H]2CCCN2C(=O)[C@H](C)NC(=O)[C@H](C)NC1=O"
        "CHPSAR_I": "CN1CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC1=O",
        "COHVAW_I": "C=C1C(=O)O[C@@H]2C/C(COC(C)=O)=C\CC[C@](C)(O)C[C@@H](OC(=O)/C(=C\C)COC(C)=O)[C@@H]12",
        "FGG55": "N[C@H](Cc1ccccc1)C(=O)NCC(=O)NCC(=O)O",
        "GFA01": "C[C@@H](NC(=O)[C@H](Cc1ccccc1)NC(=O)CN)C(=O)O",
        "GGF01": "NCC(=O)NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O",
        "GS464992_I": "COC(=O)[C@@H]1CCCN(C(=O)[C@H](Cc2cccc(O)c2)NC(=O)[C@@H](NC(C)=O)C(C)C)N1",
        "GS557577_I": "CO[C@@H]1CC/C=C/c2cccc(c2)COC(=O)[C@@H]2CCCN(N2)C(=O)[C@H](Cc2cccc(O)c2)NC(=O)[C@H](C(C)C)NC(=O)[C@@H]1C"
        "POXTRD_I": "O=C1COCC(=O)OCC(=O)NCCOCCN1"
        "SANGLI_I": "CC(=O)CC[C@H]1C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](Cc2cccc(O)c2)C(=O)N2CCC[C@H](N2)C(=O)OCC/C=C/C=C/[C@H](O)[C@H](C)[C@H]1O"
        "WG01": "N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)O"
        "WGG01": "N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O"
        "YIVNOG_I":
        }

