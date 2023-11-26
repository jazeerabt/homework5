import random
import configparser


def read_initial_money():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['GAME']['MY_MONEY'])


def calculate_result(selected_slot, bet_amount):
    winning_slot = random.randint(1, 30)
    if selected_slot == winning_slot:
        return bet_amount * 2
    return -bet_amount


def play_game():
    money = read_initial_money()
    while True:
        print(f"Your current balance is: ${money}")
        if money <= 0:
            print("You don't have enough money to continue playing.")
            break

        selected_slot = int(input("Choose a slot number (1-30): "))
        bet_amount = int(input("Enter your bet amount: "))

        if bet_amount > money:
            print("You can't bet more than you have.")
            continue

        money_change = calculate_result(selected_slot, bet_amount)
        money += money_change

        if money_change > 0:
            print(f"Congratulations! You won ${money_change}.")
        else:
            print(f"Sorry, you lost ${abs(money_change)}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    if money > read_initial_money():
        print(f"Congratulations! You won ${money - read_initial_money()} in total.")
    elif money < read_initial_money():
        print(f"Sorry! You lost ${read_initial_money() - money} in total.")
    else:
        print("You finished with the same amount of money you started with.")


if __name__ == "__main__":
    play_game()