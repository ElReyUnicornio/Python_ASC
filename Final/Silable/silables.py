import re

vocals = "aeiouáéíóú"
def vocal (char):
    if char in vocals:
        return True
    else:
        return False
        
def silables(words):
    words = words.lower()
    message = ""

    #silabas por pares
    consCount = 0

    for i,x in enumerate(words):
        if x == " ":
            message += "\n"
            continue
        if consCount >= 2:
            message += " "
        
        next = "$" if i == len(words) - 1 else words[i + 1] 
        next2 = "$" if i >= len(words) - 2 else words[i + 2] 
        back = "$" if i == 0 else words[i - 1]
        
        #default
        if next == " ":
            message += x
            consCount = 0
            continue
        if i == len(words) - 1:
            message += x
            continue
        
        #consonante
        if not vocal(x) and next != "":
            #Digrafos
            if (x == "r" and next == "r") or (x == "l" and next == "l") or (x == "c" and next == "h") or (x == "g" and next == "u") or (x == "q" and next == "u") or (x == "p" and next == "s"):
                message += " " + x
                consCount = 0
                continue
            if (x == "r" and back == "r") or (x == "l" and back == "l") or (x == "h" and back == "c"):
                message += x
                continue
            
            #consonantes compatibles
            if (x == "p" or x == "b" or x == "d" or x == "t" or x == "g" or x == "c" or x == "f" or x == "k") and (next == "r" or next == "l"):
                message += " " + x
                consCount = 0
                continue
            if (back == "p" or back == "b" or back == "d" or back == "t" or back == "g" or back == "c") and (x == "r" or x == "l"):
                message += x
                continue
            #generales
            if vocal(next):
                message += x
            elif not vocal(next) and not vocal(next2) :
                message += x
                consCount += 1
            elif not vocal(next) and vocal(next2):
                message += x + " "
                consCount = 0
        #vocal
        if vocal(x):
            message += x
            if (x == "u" and back == "g") or (x == "u" and back == "q"):
                continue
            
            #Hiatos
            if x in "íú" and vocal(next):
                message += " "
                
            #diptongo
            #creciente
            if x in "iu" and next in "aeoáéó":
                continue
            #decreciente
            if x in "aeo" and next in "iu":
                continue
            
            if (vocal(next) and not vocal(next2)) or ( not vocal(next) and vocal(next2)):
                message += " "
                consCount = 0
    
    slbs = message.split("\n")
    #se normaliza el texto de cada palabra
    for i, x in enumerate(slbs):
        slbs[i] = x.strip()
        slbs[i] = re.sub(r'\s{2,}', " ", slbs[i])
        
    return slbs