import re
nums = input("Introduce los numeros\n") 
nums = nums.replace(" ", "")
count = len(re.findall("([0-9]0[0-9]){1}", nums))
print("se encontraron 3 ceros entre los numeros" ,count)