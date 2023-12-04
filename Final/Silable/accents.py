def Get_tonics_index (words):
    tonic = []
    for x in words:
        silables = x.split(" ")
        if len(silables) == 1:
            tonic.append(1)
            continue
        if "á" in x or "é" in x or "í" in x or "ó" in x or "ú" in x:
            for i in range(len(silables) - 1, -1, -1):
                y =  silables[i]
                if "á" in y or "é" in y or "í" in y or "ó" in y or "ú" in y:
                    tonic.append(len(silables) - i)
                    break
        else:
            #Para cuando la palabra no tiene acentos
            if silables[len(silables) - 1][len(silables[len(silables) - 1]) - 1] in "aeiouns":
                tonic.append(2)
                continue
            else:
                tonic.append(1)
                continue
    return tonic

def Get_tonics (words, tonics):
    tonics_slbs = []
    for i, x in enumerate(words):
        silables = x.split(" ")
        index = -tonics[i]
        tonics_slbs.append(silables[index])
    return tonics_slbs

def Get_clasification(tonics):
    classifications = []
    for x in tonics:
        if x == 1:
            classifications.append("aguda")
            continue
        if x == 2:
            classifications.append("grave")
            continue
        if x == 3:
            classifications.append("esdrújula")
            continue
        if x >= 4:
            classifications.append("sobreesdrújula")
            continue
        if x == -1:
            classifications.append("No es posible encontrar una silaba tónica")
            continue
    return classifications;