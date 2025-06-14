def check_vowels():
    nombre = input().lower()
    for vocal in "aeiou":
        print(f"Contiene {vocal}: {vocal in nombre}")
