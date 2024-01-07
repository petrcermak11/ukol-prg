# Najděte největší číslo v poli

nejvetsi=[17,30,6,1,0,128,683,682]

nejvetsi_cislo = nejvetsi[0]

for x in nejvetsi:
    if x > nejvetsi_cislo:
        nejvetsi_cislo = x

print(nejvetsi_cislo)