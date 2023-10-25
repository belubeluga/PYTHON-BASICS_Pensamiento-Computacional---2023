#%% ejercicio 3
family_tree = {
    "a": (),
    "b": (),
    "c": ("a", "b"),
    "d": ("a", "b"),
    "e": ("a", "b"),
    "f": ("m", "n"),
    "g": ("f", "c"),
    "h": ("f", "c"),
    "i": ("d",),
    "j": ("d",),
    "k": (),
    "l": ("j", "k"),
    "m": (),
    "n": (),
}

def es_ancestro(apellido1,apellido2, arbol):
    if apellido1 in arbol[apellido2]:
        return True
    if not arbol[apellido2]:
        return False
    
    padres = arbol[apellido2]
    for padre in padres:
        es = es_ancestro(apellido1, padre, arbol)
        if es:
            return True
    return False
print(es_ancestro("m","f",family_tree))