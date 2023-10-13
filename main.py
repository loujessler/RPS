import sys

from art import text2art

from utils.secret import Secret
from utils.rules import Rules
from utils.menu import Menu


# Check command-line arguments
if sys.argv[-1][0] == '-' and sys.argv[-1] == '-mterm':
    mterm = True
    sys.argv.pop()
else:
    mterm = False
if len(sys.argv) < 4 or len(sys.argv) % 2 == 1:
    print("Error: Please provide an odd number of unique choices (>= 3) as command-line arguments.")
    sys.exit(1)


def game():
    menu_title = text2art(text="RPS Game", font="cybermedium", space=1)
    # user_choice = None
    args = sys.argv[1:]
    game_rules = Rules(args)

    # TODO: 1) генерирует криптографически стойкий случайный ключ
    key = Secret.generate_key(32)
    # TODO: 2) делает свой ход
    computer_choice = Secret.generate_comp_choice(args)
    # TODO: 3) вычисляет HMAC (на базе SHA2 или SHA3) от хода как сообщения со сгенерированным ключом
    hmac = Secret.calculate_hmac(key, computer_choice)

    menu_title = menu_title + "Available choices:" + "\nHMAC: " + hmac
    menu = Menu(args, menu_title, game_rules)
    # TODO: 4) показывает пользователя HMAC
    # TODO: 5) пользователь получает "меню" 1 - Камень, 2 - Ножницы, ...., 0 - Exit.
    # TODO: 6) Пользователь делает свой выбор (при некорректном вводе опять отображается "меню")
    user_choice = menu.show_term_menu() if mterm else menu.show_classic_menu()

    # TODO: 7) Скрипт показывает ход компьютера.
    user_choice = args[user_choice]
    print(f"Your move: {user_choice}\nComputer move: {computer_choice}")

    # TODO: 8) Скрипт показывает кто победил.
    print(f"It's {game_rules.determine_winner(user_choice, computer_choice)}!")

    # TODO: 9) Скрипт показывает исходный ключ.
    print(f"HMAC Key: {key.hex()}")

    input("\nPress Enter to continue...")


if __name__ == "__main__":
    while True:
        game()
