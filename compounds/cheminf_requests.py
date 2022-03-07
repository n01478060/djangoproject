import requests
csmiles = 'CCCC'

"""prints the URL to the pubchem rest API for that compound"""
API_URL_json = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/json"
# print(API_URL_json)

"""Use the request package to access the data at that URL"""
query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/json")
# print(query_json)
# print(query_json.text)
# print(query_json.json())


"""Use the request package to access the synonyms for the compound"""
synonym_query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/synonyms/json")
# print(synonym_query_json.json())
inchikey = 'RYYVLZVUVIJVGH-UHFFFAOYSA-N'
g = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+inchikey+"/property/MolecularWeight/json")

# synonyms = g.json()["InformationList"]["Information"][0]["MolecularWeight"]
print(g.json()["PropertyTable"]["Properties"][0]["MolecularWeight"])
