# ML-solubility-predictor

OLD MODEL (see for more info on the project): 

https://github.com/eddiechen-star/ML-solubility-predictor-old

If you find any improvements or any bugs in the code, please tell me.

# Change Log

- Created a "Classifying" file to determine whether a user input is a SMILE or molecule name to fix the bug where "cco" was passing as a molecule name.

- Added a "Featuring" file to bump the R2 score from around a 70 to a 90, the mean absolute error from 60 to 50, and the mean squared error from 70 to 60.

- Fixed a weird bug where the SMILE for amygdalin was returning None by using: from urllib.parse import quote, url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{quote(smile)}/cids/JSON".

- Made the model understand miscibility by adding an if statement to see if the predicted log s is more than or equal to -0.5.

# Installation

ML Solubility Predictor requires:
- Python (>= 3.11)
- RDKit (>= 2026.03.03)
- Pandas (>= 3.0.3)
- NumPy (>= 2.5.0)
- SKlearn/SciKit-learn (1.9.0)
- Requests (>= 2.34.2)

Before running, make sure you have Git for windows installed. You can do this at the site:

https://git-scm.com/install/windows

or using this command:

```bash
winget install --id Git.Git
```

OR if you don't want to install Git for windows download the repository as a ZIP file and extract it.

## How to run

To run ML Solubility Predictor, open a new command prompt window, clone the repository and install the required libraries:

```bash
git clone https://github.com/eddiechen-star/ML-solubility-predictor.git
cd ML-solubility-predictor
cd "Molecular Property Predictor"
pip install pandas numpy scikit-learn rdkit requests 
py ML-solubility-predictor.py

```
