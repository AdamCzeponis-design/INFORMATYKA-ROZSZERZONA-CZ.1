for liczba in range(1, 20):
    if liczba % 7 == 0:
        print(f"Znaleziono pierwszą liczbę podzielną przez 7: {liczba}")
        break
    print(f"Sprawdzam liczbę: {liczba}")

print("Koniec przeszukiwania.")