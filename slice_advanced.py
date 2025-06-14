def slice_advanced():
    texto = "Awesome".lower()
    mitad = len(texto) // 2
    print(texto[:3])                      # primeras 3 letras
    print(texto[mitad - 1:mitad + 2])     # 3 letras del medio
    print(texto[:4] + texto[-3:])         # de la primera a la cuarta + últimas 3
