import json

from pyzotero import zotero
from bibtexparser import dump

with open("zotero.json") as f:
    vars = json.load(f)

zot = zotero.Zotero(vars["user_id"], "user", vars["api_key"])
with open(vars["output"], "w") as f:
    dump(zot.everything(zot.collection_items(vars["collection_id"], format="bibtex")), f)