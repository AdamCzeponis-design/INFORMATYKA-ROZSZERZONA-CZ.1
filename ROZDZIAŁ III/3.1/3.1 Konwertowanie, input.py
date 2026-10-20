# Pobieranie danych od użytkownika (zawsze jako str)
wejscie_wiek = input("Podaj swój wiek: ")

# Konwersja (rzutowanie) tekstu na liczbę całkowitą (int)
wiek = int(wejscie_wiek)

# Obliczenie wieku za rok
wiek_za_rok = wiek + 1
print(f"Za rok będziesz mieć {wiek_za_rok} lat!")