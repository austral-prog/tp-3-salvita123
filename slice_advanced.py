def slice_advanced():
    texto = "Awesome".lower()
    print(texto[:3])                          # awe
    print(texto[len(texto)//2 - 1:len(texto)//2 + 2])  # eso
    print(texto[:4] + texto[-3:])             # awesome
