for i in range (0,3):
    correct = "Tokyo"

    answer = input("What's the capital of Japan: ")
    if answer == correct:
        print("Applause!")

    elif answer != correct:
        i = i + 1
        print("Wrong. Try again...")

    if i == 3:
        print("You failed the test. Go study Japan's geography!")




        