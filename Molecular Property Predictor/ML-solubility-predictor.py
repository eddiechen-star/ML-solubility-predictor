# measured log solubility in mols per litre

import time
start_time = time.perf_counter()

from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from utilities.extracting import extract
from utilities.training import train
from utilities.splitting import split
from utilities.fingerprint import converting
from utilities.translating import translate
from utilities.classifying import classify
from utilities.featuring import miscible
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

# 5. Model info
end_time = time.perf_counter()
print("Model trained!")
print("Time taken:", (end_time - start_time), "seconds")
print("Mean absolute error:", mean_absolute_error(y_test, model.predict(x_test)))
print("Mean squared error:", mean_squared_error(y_test, model.predict(x_test)))
print("R2 score:", r2_score(y_test, model.predict(x_test)))
print("Predicting measured log solubility in moles per litre under standard conditions.")

# 6. Test or use model
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
            if miscible(tsmiles) == "Miscible":
                print("Miscible in water.")
                continue
            print("Predicted solubility:", model.predict(converting([tsmiles])))
            print(f"SMILE for {smiles}:", tsmiles)
        except (ValueError, TypeError) as e:
            print("Invalid molecule name. Try again.")
    elif csmiles == "SMILES":
        try:
            if miscible(smiles) == "Miscible":
                print("Miscible in water.")
                continue
            print("Predicted solubility:", model.predict(converting([smiles])))
            print(f"Name for {smiles}:", tsmiles)
        except (ValueError, TypeError) as e:
            print("Invalid SMILES. Try again.")