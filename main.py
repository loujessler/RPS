import sys
from art import text2art

from utils.secret import Secret
from utils.rules import Rules
from utils.menu import Menu
from utils.validator import Validator


def main():
    validator = Validator(sys.argv[1:])
    if validator.is_empty() or not validator.is_valid():
        print(f"Error: {validator.error_message}")
        sys.exit(1)

    while True:
        game(validator)


def game(validator):
    args = validator.args
    key = Secret.generate_key(32)
    computer_choice = Secret.generate_comp_choice(args)
    hmac = Secret.calculate_hmac(key, computer_choice)

    title = text2art(text="RPS Game", font="cybermedium", space=1)
    game_rules = Rules(args)
    menu_title = f"{title}HMAC: {hmac}\n\nAvailable choices:"

    menu = Menu(args, menu_title, game_rules)
    user_index_choice = menu.show_classic_menu() if validator.classic_menu else menu.show_term_menu()
    user_choice = args[user_index_choice]

    print(f"Your move: {user_choice}\n"
          f"Computer move: {computer_choice}\n\n"
          f"{7 * '*'} {game_rules.determine_winner(user_choice, computer_choice).upper()}! {7 * '*'}\n\n"
          f"HMAC: {hmac}\n"
          f"HMAC Key: {key.hex()}")

    input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
