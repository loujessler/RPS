class Validator:
    def __init__(self, args: list):
        self.args = args
        self.error_message = None
        self.classic_menu = False

    def is_valid(self):
        """
        Func check is valid.
        :return: True if valid, False otherwise.
        """
        self._validate_cmenu()
        return self._validate_uniqueness() and self._is_valid_argument_count() and self._is_odd_argument()

    def _validate_cmenu(self):
        if self.args[-1] == '-cmenu':
            self.classic_menu = True
            self.args.pop()

    def _is_valid_argument_count(self):
        """
        Check if the number of arguments is at least 3.
        :return: True if valid, False otherwise.
        """
        if len(self.args) < 3:
            self.error_message = "The number of arguments should be at least 3."
            return False
        return True

    def _is_odd_argument(self):
        """
        Check if the number of arguments is odd.
        :return: True if valid, False otherwise.
        """
        if len(self.args) % 2 == 0:
            self.error_message = "The number of arguments should be odd."
            return False
        return True

    def _validate_uniqueness(self):
        """
        Func check unique args.
        :return: True if valid, False otherwise.
        """
        unique_args = set()
        for arg in self.args:
            if arg in unique_args:
                self.error_message = f"The argument '{arg}' is repeated."
                return False
            unique_args.add(arg)
        return True
