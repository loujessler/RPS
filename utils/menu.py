import sys
from simple_term_menu import TerminalMenu

from utils.table import TableGenerator


class Menu:
    def __init__(self, args: list, menu_title: str, game_rules: object):
        self.args = args
        self.menu_title = menu_title
        self.game_rules = game_rules
        self._user_choice = None
        self._menu_items = [f"[{i}] {item}" for i, item in enumerate(args, start=1)]

    def _display_help(self):
        """
        Show help table.
        :return:
        """
        print(TableGenerator(self.args, self.game_rules).generate_table())
        self._user_choice = None

    def _is_valid_choice(self) -> bool:
        """
        Checks if the input value exists?
        :return: Bool
        """
        return self._user_choice in [str(i + 1) for i in range(len(self.args))]

    def _display_invalid_message(self, message: str):
        """
        Show error message.
        :param message:
        :return: None
        """
        print(message)
        self._user_choice = None

    def show_term_menu(self) -> int:
        """
        Show and parse choice in term menu.
        :return: Index of item
        """
        sys_items = ['', '[?] help', '[0] exit']
        menu_entries = self._menu_items + sys_items
        menu = TerminalMenu(menu_entries=menu_entries,
                            title=self.menu_title,
                            skip_empty_entries=True,
                            menu_cursor="→",
                            cycle_cursor=True,
                            clear_screen=True)

        while self._user_choice is None:
            self._user_choice = menu.show()
            chosen_item = menu.chosen_menu_entry

            if chosen_item == 'exit':
                sys.exit(0)
            elif chosen_item == 'help':
                self._display_help()
                input("Press Enter to continue...")

        return self._user_choice

    def show_classic_menu(self) -> int:
        """
        Show and parse choice in classic menu.
        :return: Index of item
        """
        print(self.menu_title)
        [print(f"{i} - {item}") for i, item in enumerate(self.args, start=1)]
        print("\n0 - Exit"
              "\n? - Help")

        while self._user_choice is None:
            self._user_choice = input("Enter your choice: ")
            if self._user_choice == '0':
                sys.exit(0)
            elif self._user_choice == '?':
                self._display_help()
            elif self._is_valid_choice():
                print('\n')
                return int(self._user_choice) - 1
            else:
                self._display_invalid_message("Invalid choice. Please choose a valid option.")
