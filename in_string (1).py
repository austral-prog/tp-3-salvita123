nombre = input("Ingrese su nombre: ")
vocales = "aeiou"
for vocal in vocales:
	contiene = vocal in nombre.lower()
	print(f"Contiene {vocal}: {contiene}")





