import requests

def pubchem_name_to_smiles(name):
    # name to cid
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    try:
        cid = r.json()["IdentifierList"]["CID"][0]
    except (KeyError, IndexError):
        return None

    # cid to smiles
    url2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IsomericSMILES/JSON"
    r2 = requests.get(url2)

    if r2.status_code != 200:
        return None

    try:
        prop = r2.json()["PropertyTable"]["Properties"][0]
        if "IsomericSMILES" in prop:
            return prop["IsomericSMILES"]
        elif "SMILES" in prop:
            return prop["SMILES"]
    except (KeyError, IndexError):
        return None