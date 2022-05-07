def quiz_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for k in questions:
        print("----------------------------------------------")
        print(k)

        for o in options[question_number-1]:
            print(o)

        guess = input("Enter the correct option (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(k), guess)
        question_number += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(correct_guesses, guesses):
    print("----------------------------------")
    print("RESULT")
    print("----------------------------------")

    print("Answer: ", end="")
    for v in questions:
        print(questions.get(v), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score)+"%")


def play_again():

    response = input("Do you want to play again? (Y OR N): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False


questions = {
    "What is the project's name? ": "D",
    "What is the name of the project manager? ": "B",
    "What is the name of the construction manager? ": "A",
    "What is the name of the HSE Engineer? ": "C"
}


options = [
    ["A. Museum of the future", "B. Dubai Creek",
        "C. Burj Al Arab", "D. RAK Mangrove Hotel"],
    ["A. Engr S.D", "B. Engr F.Y", "C. Engr G.A", "D. Engr K.H"],
    ["A. Engr K.H", "B. Engr G.A", "C. Engr S.D", "D. Engr F.Y"],
    ["A. Engr F.Y", "B. Engr K.H", "C. Engr S.D", "D. Engr G.A"]
]


quiz_game()


while play_again():
    quiz_game()

print("THE LAST SCORE WILL BE RECORDED AS YOUR ASSESSMENT RESULT.")
