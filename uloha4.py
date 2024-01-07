# Mám kbelík s množstvím tmavě modré barvy a rád bych namaloval co nejvíce stěn.
#Vytvořte funkci, která vrátí počet úplných stěn, které mohu vymalovat, než budu muset zamířit do obchodů a koupit si další.
# n je počet metrů čtverečních, které mohu namalovat.
# w a h jsou šířky a výšky jedné stěny v metrech.

def my_function(n,w,h):
    x= n/(w*h)
    return x 

print(my_function(100,4,5))