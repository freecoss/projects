notes = {"math":15,"python":13.5,"francais":16}
notes["math"] = 18
print(notes)
notes.update({"python":0,"java":17})
print(notes)
print(notes["francais"])
print(notes.get("franais","element introuvable!"))
print(notes.keys())
print(notes.values())
print(notes.items())
notes.pop("java")
print(notes)
notes.popitem()
for elt in notes:
    print(elt)
for matiere,note in notes.items():
    print(f"la note de la matiere {matiere} est {note}")