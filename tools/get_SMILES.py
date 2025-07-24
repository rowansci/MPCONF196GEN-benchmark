import os
import numpy as np
import ase.io
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


def mol_from_ase_atoms(atoms, tol: float = 0.45) -> Chem.Mol:
    """
    Build an RDKit Mol from an ASE Atoms by
    adding single bonds whenever dist < cov_rad_i + cov_rad_j + tol.
    """
    syms   = atoms.get_chemical_symbols()
    coords = atoms.get_positions()
    pt     = Chem.GetPeriodicTable()
    rw     = Chem.RWMol()

    # add atoms
    for sym in syms:
        rw.AddAtom(Chem.Atom(sym))

    # add bonds by distance threshold
    n = len(syms)
    for i in range(n):
        for j in range(i+1, n):
            d  = np.linalg.norm(coords[i] - coords[j])
            ri = pt.GetRcovalent(syms[i])
            rj = pt.GetRcovalent(syms[j])
            if d < (ri + rj + tol):
                rw.AddBond(i, j, Chem.BondType.SINGLE)

    mol = rw.GetMol()
    Chem.SanitizeMol(mol)
    return mol


def smiles_and_rotatable_from_xyz(xyz_path: str) -> tuple[str,int]:
    """
    Read first frame of an ext‑XYZ, convert via ASE→RDKit,
    drop explicit Hs, and return (canonical SMILES, # rotatable bonds).
    """
    atoms = ase.io.read(xyz_path, index=0, format="extxyz")
    mol = mol_from_ase_atoms(atoms)
    # remove explicit Hs and sanitize
    mol2 = Chem.RemoveHs(mol, updateExplicitCount=True)
    Chem.SanitizeMol(mol2)

    smi   = Chem.MolToSmiles(mol2, canonical=True)
    n_rot = rdMolDescriptors.CalcNumRotatableBonds(mol2)
    return smi, n_rot


def print_smiles_table(molecules_dir="molecules"):
    """
    Scan each subfolder for crest_conformers.xyz and print:
    Rotatable_Bonds    SMILES    Molecule_Name
    """
    print("Rotatable_Bonds\tSMILES\tMolecule_Name")
    for sub in sorted(os.listdir(molecules_dir)):
        xyz = os.path.join(molecules_dir, sub, "crest_conformers.xyz")
        if os.path.isfile(xyz):
            smi, n_rot = smiles_and_rotatable_from_xyz(xyz)
            print(f"{n_rot}\t{smi}\t{sub}")


if __name__ == "__main__":
    print_smiles_table("molecules")

