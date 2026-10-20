posiada_bilet = True
posiada_zniżkę = False
jest_weekend = True

# Operator and (wszystko musi być prawdą)
# Np. wejście na strefę VIP wymaga biletu I zniżki (tutaj będzie False)
wejscie_vip = posiada_bilet and posiada_zniżkę 

# Operator or (wystarczy jeden warunek)
# Np. darmowy wstęp, jeśli jest weekend LUB posiada zniżkę
darmowy_wstep = jest_weekend or posiada_zniżkę

# Operator not (odwrócenie wartości)
brak_biletu = not posiada_bilet

print(f"Dostęp do strefy VIP: {wejscie_vip}")
print(f"Darmowy wstęp: {darmowy_wstep}")
print(f"Brak biletu: {brak_biletu}")