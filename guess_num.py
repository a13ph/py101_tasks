import random

if __name__ == '__main__':
    # Программа генерирует число от 0 до 1_000_000
    secret_number = random.randint(1, 1_000_000)

    # Программа приветствовует пользователя
    print("Hello Dave! Would you like to play a little game?\n")

    # Программа предлагает угадать его.
    print("Guess a number between one and...",
          "a million! *holds pinky to lips*",
          "\nType 'exit' or submit empty guess to finish the game.", sep="\n")

    guess = None
    while not guess == secret_number:
        # Программа считывает число с клавиатуры
        try:
            input_string = input("\nPlease enter your guess: ")
            if input_string == "exit" or input_string == "":
                exit()
            guess = int(input_string)
        except ValueError:
            print("Your guess should be a number")
            exit
        # пользователь ввёл пустую строку - выход из программы
        except SyntaxError:
            guess = "exit"
        else:
            # пользователь ввёл exit - выход из программы
            if guess == "exit":
                exit()
            # пользователь ввёл не целое число
            elif not type(guess) is int:
                print("Oh, hey! Your input must be an number,")
                print("integer between 1 and 1 000 000 to be exact!")
            # число не входит в обозначенный в условии диапазон
            elif guess < 0 or guess > 1_000_000:
                print("Your guess is out of bounds.",
                      "My number is between 1 and 1 000 000", sep="\n")
            elif guess > secret_number:
                print("No, your guess is too high.")
            elif guess < secret_number:
                print("No, your guess is too low.")
            elif guess == secret_number:
                print("Yup, that's correct!")
            else:
                print("IDK how you did that, please report a bug")
