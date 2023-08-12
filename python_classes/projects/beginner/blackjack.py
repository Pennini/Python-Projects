from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose, you went over"
    elif user_score == 0:
        return "Win, you have a blackjack"
    elif computer_score == 0:
        return "Lose, computer has a blackjack"
    elif user_score > 21:
        return "Lose, you went over"
    elif computer_score > 21:
        return "Win, computer went over"
    elif user_score > computer_score:
        return "Win"
    elif user_score < computer_score:
        return "Lose"
    else:
        return "Draw"


def calculate_score(list):
    sum_list = sum(list)
    if sum_list == 21 and len(list) == 2:
        return 0
    if 11 in list and sum_list > 21:
        list.remove(11)
        list.append(1)
        sum_list = sum(list)
    return sum_list


def play_game():
    #   print(logo)
    user_cards = []
    computer_cards = []
    is_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    result_player = calculate_score(user_cards)
    result_computer = calculate_score(computer_cards)

    while not is_over:
        result_player = calculate_score(user_cards)
        result_computer = calculate_score(computer_cards)
        print(
            f"Your cards: {user_cards}, current score: {result_player}\nComputer's first card: {computer_cards[0]}"
        )

        if result_player == 0 or result_computer == 0 or result_player > 21:
            is_over = True
        else:
            play_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_again == "y":
                user_cards.append(deal_card())
            else:
                is_over = True
    while result_computer < 17 and result_computer != 0:
        computer_cards.append(random.choice(cards))
        result_computer = calculate_score(computer_cards)

    print(
        f"Your final hand: {user_cards}, final score: {result_player}\nComputer's first hand: {computer_cards}, final score: {result_computer}"
    )
    print(compare(result_player, result_computer))


while input('Do you want to play a game of blackjack? Type "y" or "n": ') == "y":
    clear()
    play_game()
