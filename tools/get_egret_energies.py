import os

import ase.io
import torch
from ase.calculators.calculator import all_changes
from mace.calculators import mace_off

KCAL_PER_MOL = 23.0605
MOLECULES_DIR = "molecules"

calc = mace_off(model="tools/EGRET_1.model", default_dtype="float64")


def process_subdir(subdir: str) -> None:
    in_xyz  = os.path.join(subdir, "crest_conformers.xyz")
    out_xyz = os.path.join(subdir, "crest_conformers_egret.xyz")

    all_confs = ase.io.read(in_xyz, format="xyz", index=":")
    for atoms in all_confs:
        calc.calculate(atoms, ["energy"], all_changes)
        atoms.info["energy"] = calc.results["energy"] * KCAL_PER_MOL

    ase.io.write(out_xyz, all_confs, format="extxyz")
    print(f"wrote {out_xyz}")


def main() -> None:
    for sub in sorted(os.listdir(MOLECULES_DIR)):
        subpath = os.path.join(MOLECULES_DIR, sub)
        if os.path.isdir(subpath) and os.path.exists(os.path.join(subpath, "crest_conformers.xyz")):
            print(f"Processing {sub} …")
            process_subdir(subpath)
        else:
            print(f"Skipping {sub!r}")


if __name__ == "__main__":
    main()
