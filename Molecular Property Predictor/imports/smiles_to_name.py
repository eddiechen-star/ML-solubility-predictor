import requests

def pubchem_smiles_to_name(smile):
    # smile to cid
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smile}/cids/JSON"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    try:
        cid = r.json()["IdentifierList"]["CID"][0]
    except (KeyError, IndexError):
        return None

    # cid to smiles
    url2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName/JSON"
    r2 = requests.get(url2)

    if r2.status_code != 200:
        return None

    try:
        prop = r2.json()["PropertyTable"]["Properties"][0]
        return prop["IUPACName"]
    except (KeyError, IndexError):
        return None
