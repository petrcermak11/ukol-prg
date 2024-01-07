# Zjistěte kolik je ve větě slov.

veta="Šel pes do lesa a potkal dlažební kostku."
count=0
for x in veta:
    if x == " ":
        count+=1
    elif x== ".":
        count+=1
    elif x== "!":
        count+=1
    elif x== "?":
        count+=1
    elif x== ",":
        count+=1
print(count)