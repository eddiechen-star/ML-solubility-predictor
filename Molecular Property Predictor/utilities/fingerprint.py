import numpy as np # arrays/math
from rdkit import Chem # molecules
from imports.fp_gen import fp_gen

# Turning the smiles into something that a machine can understand
def converting(x):
    x_features = []
    for smile in x:
        mol = Chem.MolFromSmiles(smile) # Converts a SMILES string into a RDKit molecule object that the computer can understand
        fp_bit_vector = fp_gen.GetFingerprint(mol) # Generates a molecular fingerprint
        fp_array = np.zeros((2048,), dtype=np.int8) # Makes an empty array to store the fingerprints
        Chem.DataStructs.ConvertToNumpyArray(fp_bit_vector, fp_array) # Fills that empty array with the fingerprint values
        x_features.append(fp_array) # adds to features
    x_features = np.array(x_features) # converts the list of fingerprint arrays into a single NumPy matrix so ml models can use it.
    return x_features