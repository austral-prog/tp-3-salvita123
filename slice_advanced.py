def slice_texto():
    texto = "Awesome".lower()  # Nos aseguramos de que esté en minúsculas
    mitad = len(texto) // 2
    print(texto[:3])                 # Primeras 3 letras
    print(texto[mitad - 1:mitad + 2])  # 3 letras del medio
    print(texto[:4] + texto[-3:])   # Primera a cuarta + antepenúltima a última
