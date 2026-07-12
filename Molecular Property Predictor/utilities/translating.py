from utilities.classifying import classify
from imports.name_to_smiles import pubchem_name_to_smiles
from imports.smiles_to_name import pubchem_smiles_to_name

# memory for translated smiles and names (too lazy to make a new datafile)
name_cache = {}
smiles_cache = {}

def translate(smiles):
    clean = smiles.lower().strip()

    # cached name lookup
    if clean in name_cache:
        return name_cache[clean]
    if smiles in smiles_cache:
        return smiles_cache[smiles]

    # classify
    csmiles = classify(smiles)
    # if classified as smiles
    if csmiles == "SMILES":
        name = pubchem_smiles_to_name(smiles)
        if name:
            smiles_cache[smiles] = name
        return name

    # if classified as name
    if csmiles == "Name":
        translated = pubchem_name_to_smiles(clean)
        if translated:
            name_cache[clean] = translated
        return translated
