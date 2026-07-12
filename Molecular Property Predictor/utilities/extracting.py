import pandas as pd
import os

def extract():
    file_path = "data/df_clean.csv"

    # If the cleaned dataset already is saved, load it
    if os.path.exists(file_path):
        df_clean = pd.read_csv(file_path)

    else:
        url = "https://raw.githubusercontent.com/deepchem/deepchem/master/datasets/delaney-processed.csv"
        df = pd.read_csv(url)

        # Cleaning data
        df_clean = df[df["smiles"].notnull()].reset_index(drop=True)

        # Making sure the folder exists
        os.makedirs("data", exist_ok=True)

        # Saving the cleaned version for next time
        df_clean.to_csv(file_path, index=False)

    # Always return the same outputs
    y = df_clean["measured log solubility in mols per litre"]
    x = df_clean["smiles"]

    return x, y