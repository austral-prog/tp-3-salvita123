def slice_advanced():
    texto = "Awesome".lower()
    mitad = len(texto) // 2
    print(texto[:3])
    print(texto[mitad - 1:mitad + 2])
    print(texto[:4] + texto[-3:])
