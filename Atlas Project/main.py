from datetime import datetime
from country_checker import CountryChecker


starting_letter = "s"
player_num = 2
game_over = False
while not game_over:
    if player_num == 2:
        player_num = 1
    else:
        player_num = 2
    time = datetime.now()
    new_country = CountryChecker(player_num, 1)
    num_incorrect = 0
    game_over = new_country.check_country(num_incorrect, starting_letter)
    if game_over:
        break
    print("Correct")
    second_country = CountryChecker(player_num, 2)
    game_over = second_country.check_country(num_incorrect, starting_letter)
    if game_over:
        break
    print("Correct")
    starting_letter = "".join([character for character in new_country.country[1:] if character in second_country.country[1:]])
    if len(starting_letter) > 1:
        letter1 = input("Enter a letter common to both above countries: ").strip().lower()
        while letter1 not in starting_letter:
            letter1 = input("Please enter an appropriate, common letter: ").strip().lower()
        starting_letter = letter1
    if starting_letter:
        print("The next round's starting letter is", starting_letter)
    print("\n")
    # if len(starting_letter) > 2:
    #     letter1 = input("Enter a letter common to both above countries: ").strip().lower()
    #     while letter1 not in starting_letter:
    #         letter1 = input("Please enter an appropriate, common letter: ").strip().lower()
    #     letter2 = input("Enter another letter common to both above countries: ").strip().lower()
    #     while letter2 == letter1 or letter2 not in starting_letter:
    #         if letter2 == letter1:
    #             letter2 = input("Enter a letter different from the first letter you have chosen: ").strip().lower()
    #         else:
    #             letter2 = input("Please enter an appropriate, common letter: ").strip().lower()
    #     starting_letter = letter1+letter2
