from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


SMILES = {
        "CAMVES_I": r"C[C@@H]1NC(=O)[C@H](C)NC(=O)[C@@H]2CCCN2C(=O)[C@H]2CCCN2C(=O)[C@H](C)NC(=O)[C@H](C)NC1=O",
        "CHPSAR_I": r"CN1CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC(=O)N(C)CC1=O",
        "COHVAW_I": r"C=C1C(=O)O[C@@H]2C/C(COC(C)=O)=C\CC[C@](C)(O)C[C@@H](OC(=O)/C(=C\C)COC(C)=O)[C@@H]12",
        "FGG55": r"N[C@H](Cc1ccccc1)C(=O)NCC(=O)NCC(=O)O",
        "GFA01": r"C[C@@H](NC(=O)[C@H](Cc1ccccc1)NC(=O)CN)C(=O)O",
        "GGF01": r"NCC(=O)NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O",
        "GS464992_I": r"COC(=O)[C@@H]1CCCN(C(=O)[C@H](Cc2cccc(O)c2)NC(=O)[C@@H](NC(C)=O)C(C)C)N1",
        "GS557577_I": r"CO[C@@H]1CC/C=C/c2cccc(c2)COC(=O)[C@@H]2CCCN(N2)C(=O)[C@H](Cc2cccc(O)c2)NC(=O)[C@H](C(C)C)NC(=O)[C@@H]1C",
        "POXTRD_I": r"O=C1COCC(=O)OCC(=O)NCCOCCN1",
        "SANGLI_I": r"CC(=O)CC[C@H]1C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](Cc2cccc(O)c2)C(=O)N2CCC[C@H](N2)C(=O)OCC/C=C/C=C/[C@H](O)[C@H](C)[C@H]1O",
        "WG01": r"N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)O",
        "WGG01": r"N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O",
        "YIVNOG_I": r"C1CN2CC(NCCN(CC3C=CC=CC=3)CCNC(CN3CCN(CC(NCCN(CC4C=CC=CC=4)CCNC(CN(CC2)C1)=O)=O)CCC3)=O)=O",
        }


with open("SMILES.txt", "w") as f:
    f.write("molecule_id\trotatable_bonds\tSMILES\tSMILES_with_H\n")
    for name, smi in SMILES.items():
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            print(f"Skipping {name}: invalid SMILES")
            continue
        smi_canon = Chem.MolToSmiles(mol)
        n_rot = rdMolDescriptors.CalcNumRotatableBonds(mol)

        mol_H = Chem.AddHs(mol)
        smi_with_H = Chem.MolToSmiles(mol_H)

        f.write(f"{name}\t{n_rot}\t{smi_canon}\t{smi_with_H}\n")
