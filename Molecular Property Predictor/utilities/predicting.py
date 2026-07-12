import numpy as np # arrays/math
from rdkit import Chem # molecules
from imports.fp_gen import fp_gen
from rdkit import DataStructs # store fingerprints

def predict(smiles, model):
    usermol = Chem.MolFromSmiles(smiles) # getting the mole from the user's smile
    fp_bit_vector = fp_gen.GetFingerprint(usermol) # making the fingerprint
    fp_array = np.zeros((2048,), dtype=np.int8) # making an empty array to store all the fingerprints
    DataStructs.ConvertToNumpyArray(fp_bit_vector, fp_array) # fills the empty array with the fingerprints
    fp_array = fp_array.reshape(1, -1) # reshapes it so it can be used
    return model.predict(fp_array)