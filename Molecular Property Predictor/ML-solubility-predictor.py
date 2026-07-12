# measured log solubility in mols per litre

import time
start_time = time.perf_counter()

from utilities.extracting import extract
from utilities.predicting import predict
from utilities.training import train
from utilities.splitting import split
from utilities.fingerprint import converting
from utilities.translating import translate
from utilities.classifying import classify
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

# 1. Get raw data
x, y = extract()

# 2. Convert molecules to 2d fingerprint matrix
x_features = converting(x)

# 3. Split into train/test sets
x_train, x_test, y_train, y_test = split(x_features, y)

# 4. Train model
model = train(x_train, y_train)

end_time = time.perf_counter()
print("Model trained!")
print("Time taken:", (end_time - start_time), "seconds")
print("Predicting measured log solubility in mols per litre under standard conditions.")

# 5. Test or use model
while True:
    smiles = input("Enter SMILES or molecular names (or 'quit'): ")
    csmiles = classify(smiles)
    tsmiles = translate(smiles)
    if smiles.lower() == 'quit':
        break
    elif not smiles:
        print("Empty SMILES.")
        continue
    elif csmiles == "Name":
        try:
            print("Predicted solubility:", predict(tsmiles, model))
            print(f"SMILE for {smiles}:", tsmiles)
        except (ValueError, TypeError) as e:
            print("Invalid SMILES. Try again.")
    elif csmiles == "SMILES":
        try:
            print("Predicted solubility:", predict(smiles, model))
            print(f"Name for {smiles}:", tsmiles)
        except (ValueError, TypeError) as e:
            print("Invalid SMILES. Try again.")