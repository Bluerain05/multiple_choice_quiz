from playsound import playsound

playsound('Fanfare-sound.mp3')


def multi_intro():
    print("**********************************************************")
    print("|              WELCOME TO TRIVIA WORLD!                  |")
    print("**********************************************************")
    print("| YOU WILL BE GIVEN FIVE RANDOM MULTIPLE CHOICE QUESTIONS|")
    print("**********************************************************")
    print("|       PICK THE CORRECT ANSWER TO EACH QUESTION         |")
    print("**********************************************************")
    print("|                     WIN POINTS!                        |")
    print("**********************************************************")


multi_intro()

player = input("Player's name: ")
print("Hello", player + "!")
print("Let's play!\n")

score = 0

while True:
    question_1 = print(
        "\n1. What type of galaxy is the Milky Way galaxy? \n" "A. Irregular\n" "B. Elliptical\n" "C. Spiral")
    choice_1 = "C"
    choice = input("Answer: ")
    if choice == choice_1:
        print("Correct! Great Job!")
        score += 1
    else:
        print("That is incorrect! It is " + choice_1 + "!\n")
    question_2 = print(
        "\n2. What is electricity composed of? \n" "A. Water\n" "B. Electrons\n" "C. Air")
    choice_2 = "B"
    choice = input("Answer: ")
    if choice == choice_2:
        print("Correct! Great Job!")
        score += 1
    else:
        print("That is incorrect! It is " + choice_2 + "!\n")
    question_3 = print(
        "\n3. Which of the following animals can run the fastest? \n" "A. Cheetah\n" "B. Leopard\n" "C. Tiger")
    choice_3 = "A"
    choice = input("Answer: ")
    if choice == choice_3:
        print("Correct! Great Job!")
        score += 1
    else:
        print("That is incorrect! It is " + choice_3 + "!\n")
    question_4 = print(
        "\n4. In the series Game of Thrones, Winterfell is the ancestral home of which family? \n" "A. The Lannisters\n" "B. The Starks\n" "C. The Tully's")
    choice_4 = "B"
    choice = input("Answer: ")
    if choice == choice_4:
        print("Correct! Great Job!")
        score += 1
    else:
        print("That is incorrect! It is " + choice_4 + "!")
    question_5 = print(
        "\n5. Which company is known for publishing the Mario video game? \n" "A. Nintendo\n" "B. SEGA\n" "C. XBOX")
    choice_5 = "A"
    choice = input("Answer: ")
    if choice == choice_5:
        print("Correct! Great Job!\n")
        score += 1
    else:
        print("That is incorrect! It is " + choice_5 + "!\n")

    print("You got " + str(score) +
          " questions correct! Score is " + str(int(score/5 * 100)) + "%\n")
    print("Thank you for playing Trivia World!\nGoodbye!")
    quit()
