tree = {
    "Elektronika": {
        "Komputery": ["Laptopy", "PC"],
        "Telefony": ["Smartfony", "Akcesoria"]
    },
    "Dom": {
        "Meble": ["Stoły", "Krzesła"]
    }
}

def walk_tree(node, prefix=""):
    if isinstance(node, dict):
        for key, value in node.items():
            walk_tree(value, prefix + key + " > ")
    elif isinstance(node, list):
        for item in node:
            print(prefix + item)

walk_tree(tree)
