# Zjistěte kolik čísel v poli je sudé a kolik liché
cisla=[6,10,2,3,7,666,3701,4,81765,2024]
suda=0
licha=0

for x in cisla:
    if x%2 == 0:
        suda+=1
    else:
        licha+=1
print("Sudých je",suda,",a lichých je",licha)