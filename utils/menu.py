import sys
from simple_term_menu import TerminalMenu

from utils.table import TableGenerator


class Menu:
    def __init__(self, args, menu_title, game_rules):
        self.args = args
        self.menu_title = menu_title
        self.game_rules = game_rules

        self.user_choice = None
        self.menu_items = [f"[{i}] {item}" for i, item in enumerate(args, start=1)]

    def show_term_menu(self):
        sys_items = ['', '[?] help', '[0] exit']
        menu = TerminalMenu(self.menu_items + sys_items,
                            title=self.menu_title,
                            skip_empty_entries=True,
                            cycle_cursor=True,
                            clear_screen=True)
        menu.show()

        while self.user_choice is None:
            # TODO: 5) пользователь получает "меню" 1 - Камень, 2 - Ножницы, ...., 0 - Exit.
            # TODO: 6) Пользователь делает свой выбор (при некорректном вводе опять отображается "меню")
            self.user_choice = menu.chosen_menu_index
            len_args = len(self.menu_items)

            if self.user_choice == len_args + 2:
                sys.exit(0)
            elif self.user_choice == len_args + 1:
                display_help = None
                while display_help is None:
                    self.user_choice = None
                    print(TableGenerator(self.args, self.game_rules).generate_table())
                    display_help = input("Press Enter to continue...")
                menu.show()

        return self.user_choice

    def show_classic_menu(self):
        print(self.menu_title)
        for i, item in enumerate(self.args, start=1):
            print(f"{i} - {item}")

        print("\n0 - Exit")
        print("? - Help")

        while self.user_choice is None:
            try:
                self.user_choice = input("Enter your choice: ")
                if self.user_choice == '0':
                    sys.exit(0)
                elif self.user_choice == '?':
                    print(TableGenerator(self.args, self.game_rules).generate_table())
                    self.user_choice = None
                elif self.user_choice in [str(i + 1) for i in range(len(self.args))]:
                    print('\n')
                    return int(self.user_choice) - 1
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                self.user_choice = None
