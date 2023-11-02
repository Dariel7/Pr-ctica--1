palabras = ("manzana", "banana", "pera", "naranja", "uva")

contador = 0

for palabra in palabras:
    contador += palabra.count('a')

print("La letra 'a' aparece", contador, "veces en total en las palabras.")
