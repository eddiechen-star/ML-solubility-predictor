# measured log solubility in mols per litre
import time
start_time = time.perf_counter()

start_time_import = time.perf_counter()
from utilities.extracting import extract
from utilities.predicting import predict
from utilities.training import train
from utilities.splitting import split
from utilities.fingerprint import converting
from utilities.translating import translate
from utilities.classifying import classify
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')  # silence RDKit noise
end_time_import = time.perf_counter()

# 1. Get raw data (SMILES + solubility)
x, y = extract()

# 2. Convert molecules → 2D fingerprint matrix
start_time_finger = time.perf_counter()
x_features = converting(x)
end_time_finger = time.perf_counter()

# 3. Split into train/test sets
start_time_split = time.perf_counter()
x_train, x_test, y_train, y_test = split(x_features, y)
end_time_split = time.perf_counter()

# 4. Train model
start_time_train = time.perf_counter()
model = train(x_train, y_train)
end_time_train = time.perf_counter()

end_time = time.perf_counter()
print("Model trained!")
print("Time taken:", (end_time - start_time), "seconds")
print("Time taken:", (end_time_finger - start_time_finger), "seconds")
print("Time taken:", (end_time_split - start_time_split), "seconds")
print("Time taken:", (end_time_train - start_time_train), "seconds")
print("Time taken:", (end_time_import - start_time_import), "seconds") 
print("Predicting measured log solubility in mols per litre under STP.")

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
            # Now the model gets clean SMILES no matter what user typed
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
