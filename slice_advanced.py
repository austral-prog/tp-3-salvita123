def slice_text():
    texto = "Awesome".lower()
    mitad = len(texto) // 2
    print(texto[:3])  # primeras 3
    print(texto[mitad - 1:mitad + 2])  # 3 del medio
    print(texto[:4] + texto[-3:])  # 0–4 y últimas 3
