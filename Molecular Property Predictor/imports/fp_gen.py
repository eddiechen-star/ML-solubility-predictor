# making fingerprints (specific things for each molecule so it's readable by the computer)
from rdkit.Chem import rdFingerprintGenerator
fp_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)