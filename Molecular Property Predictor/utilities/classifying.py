import numpy as np
from sklearn import linear_model

### TEMP bc I want a more accurate model later

def convert(x): # creates a bunch of features to be mapped to molecules and smiles later on
    features = []
    features.append(len(x)) # length
    features.append(sum(1 for c in x if c.isupper())) # uppercase
    features.append(sum(1 for c in x if c.islower())) # lowercase
    features.append(sum(1 for c in x if c.isdigit())) # numbers
    features.append(sum(1 for c in x if "=" in c)) # bonds
    features.append(sum(1 for c in x if "(" or ")" in c))  # group atoms
    features.append(sum(1 for c in x if "c" in c.lower())) # carbon atoms
    return features


def classify(user_input):
    x = np.array(["CCO", "Fc1cccc(Br)c1", "OCC3OC(OCC2OC(OC(C#N)c1ccccc1)C(O)C(O)C2O)C(O)C(O)C3O", "OCC(O)COC(=O)c1ccccc1Nc2ccnc3cc(Cl)ccc23", "Cc1cccc2c1Cc3ccccc32", "Clc1cc(Cl)c(Cl)c(c1Cl)c2c(Cl)c(Cl)cc(Cl)c2Cl", "ethanol", "aspirin", "Methyl butyrate", "6-Methylchrysene", "L-arabinose", "'3,3-Dimethyl-1-butanol'"])
    converted = []

    for i in x:
        converted.append(convert(i))

    #Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
    # (0 for "No", 1 for "Yes").
    y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

    logr = linear_model.LogisticRegression()
    logr.fit(converted,y)

    c_input = convert(user_input)
    predicted = logr.predict(np.array([c_input])) # array

    if predicted[0] == 1:
        return ("SMILES")
    else:
        return ("Name")

