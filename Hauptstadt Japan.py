for i in range (0,3):
    correct = "Tokyo"

    answer = input("Hauptstadt von Japan: ")
    if answer == correct:
        print("Gratulation!")

    elif answer != correct:
        i = i + 1
        print("Leider falsch, Noch einmal")

    if i == 3:
        print("Prüfung leider nicht bestanden")