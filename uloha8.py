# Najděte nejmenší číslo v poli

nejmensi=[17,30,6,1,0,128,683,682]

nejmensi_cislo = nejmensi[0]

for x in nejmensi:
    if x < nejmensi_cislo:
        nejmensi_cislo = x

print(nejmensi_cislo)