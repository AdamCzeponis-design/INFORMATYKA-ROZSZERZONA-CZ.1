punkty = int(input("Podaj liczbę punktów z testu (0-100): "))

if punkty >= 90:
    print("Ocena: Celujący (5)")
elif punkty >= 75:
    print("Ocena: Bardzo dobry (4)")
elif punkty >= 50:
    print("Ocena: Dostateczny (3)")
else:
    print("Ocena: Niedostateczny (2) - musisz poprawić test.")


