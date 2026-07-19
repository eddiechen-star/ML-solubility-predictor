from rdkit.Chem import Descriptors
from rdkit import Chem
import numpy as np
from sklearn import linear_model

def features(smile): # creates a bunch of features to be mapped to molecules and smiles later on
    mol = Chem.MolFromSmiles(smile)  # Converts a SMILES string into a RDKit molecule object that the computer can understand
    weight = (Descriptors.ExactMolWt(mol))
    logp = (Descriptors.MolLogP(mol))
    rbonds = (Descriptors.NumRotatableBonds(mol))
    carbons = sum(1 for c in smile if "c" in c.lower())
    # aromatic atoms
    num_aromatic_atoms = sum(1 for atom in mol.GetAtoms() if atom.GetIsAromatic())
    num_heavy_atoms = mol.GetNumHeavyAtoms()
    aromatic = num_aromatic_atoms / num_heavy_atoms if num_heavy_atoms > 0 else 0

    tpsa = Descriptors.TPSA(mol) # Topological Polar Surface Area. Polar atoms increase hydrogen bonding potential with water, raising solubility.
    mr = Descriptors.MolMR(mol) # Crippen Molar Refractivity. Measures structural polarizability, highlighting dispersion interactions.
    acid = Descriptors.NumHDonors(mol)
    base = Descriptors.NumHAcceptors(mol)
    f_csp3 = Descriptors.FractionCSP3(mol)

    feature = np.array([weight, logp, rbonds, aromatic, tpsa, mr, acid, base, f_csp3, carbons])
    return feature

def miscible(user_input):
    x = np.array(["CCO", "CC(=O)C", "CC(=O)O", "CS(=O)C", "C(C(CO)O)O", "C(CO)O", "CCCCCC", "c1ccccc1", "Cc1ccccc1", "CCCCO", "CCCCCCCCCC", "C1CCCCC1"])
    featured = []

    for i in x:
        featured.append(features(i))

    #Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
    # (0 for "No", 1 for "Yes").
    y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

    logr = linear_model.LogisticRegression()
    logr.fit(featured,y)

    c_input = features(user_input)
    predicted = logr.predict(np.array([c_input])) # array

    if predicted[0] == 1:
        return ("Miscible")
    else:
        return ("Not")