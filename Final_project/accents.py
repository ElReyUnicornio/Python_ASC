def tonics (words):
    tonic = []
    for x in words:
        if "á" in x or "é" in x or "í" in x or "ó" in x or "ú" in x:
            silables = x.split(" ")
            for i in range(len(silables) - 1, -1, -1):
                y =  silables[i]
                print(y)
                if "á" in y or "é" in y or "í" in y or "ó" in y or "ú" in y:
                    tonic.append(len(silables) - i)
                    continue
                if i == 0:
                    tonic.append(-1)
                    continue
    return tonic

def clasification(tonics):
    classifications = []
    for x in tonics:
        if x == 1:
            classifications.append("aguda")
            continue
        if x == 2:
            classifications.append("grave")
        if x == 4:
            classifications.append("esdrujula")
        if x < 4:
            classifications.append("sobreesdrujula")
        if x == -1:
            classifications.append("No es posible encontrar una silaba tónica")
    return classifications;