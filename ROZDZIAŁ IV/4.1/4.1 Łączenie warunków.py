wiek = int(input("Podaj swój wiek: "))
posiada_karta_seniora = input("Czy posiadasz kartę seniora? (tak/nie): ") == "tak"

# Użycie operatorów or oraz and w jednym warunku
if wiek < 7 or (wiek >= 65 and posiada_karta_seniora):
    print("Przysługuje Ci darmowy bilet!")
else:
    print("Musisz kupić standardowy bilet.")

