# Symulacja pętli "do while": pytamy użytkownika przynajmniej raz
while True:
    haslo = input("Podaj hasło (min. 6 znaków): ")
    if len(haslo) >= 6:
        break  # wychodzimy z pętli, gdy warunek jest spełniony
    print("Za krótkie hasło! Spróbuj ponownie.")

print("Hasło zaakceptowane!")


    