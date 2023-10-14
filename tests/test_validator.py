from unittest import TestCase

from utils.validator import Validator


class TestValidator(TestCase):
    def test_valid_argument_count(self):
        args = ["arg1", "result1", "arg2"]
        validator = Validator(args)
        result = validator._is_valid_argument_count()
        self.assertTrue(result)

    def test_invalid_argument_count(self):
        args = ["arg1", "result1"]
        validator = Validator(args)
        result = validator._is_valid_argument_count()
        self.assertFalse(result)
        self.assertEqual(validator.error_message, "The number of arguments should be at least 3.")

    def test_odd_argument_count(self):
        args = ["arg1", "result1", "arg2"]
        validator = Validator(args)
        result = validator._is_odd_argument()
        self.assertTrue(result)

    def test_even_argument_count(self):
        args = ["arg1", "result1", "arg2", "result2"]
        validator = Validator(args)
        result = validator._is_odd_argument()
        self.assertFalse(result)
        self.assertEqual(validator.error_message, "The number of arguments should be odd.")

    def test_valid_uniqueness(self):
        args = ["arg1", "result1", "arg2", "result2"]
        validator = Validator(args)
        result = validator._validate_uniqueness()
        self.assertTrue(result)

    def test_invalid_uniqueness(self):
        args = ["arg1", "result1", "arg1", "result2"]
        validator = Validator(args)
        result = validator._validate_uniqueness()
        self.assertFalse(result)
        self.assertEqual(validator.error_message, "The argument 'arg1' is repeated.")

    def test_validate_cmenu(self):
        args = ["arg1", "result1", "-cmenu"]
        validator = Validator(args)
        validator._validate_cmenu()
        self.assertTrue(validator.classic_menu)
        self.assertEqual(args, ["arg1", "result1"])

    def test_is_valid(self):
        args = ["arg1", "result1", "arg2", "result2", "result3", "-cmenu"]
        validator = Validator(args)
        result = validator.is_valid()
        self.assertTrue(result)

    def test_invalid_is_valid(self):
        args = ["arg1", "result1", "arg1", "result2", "-cmenu"]
        validator = Validator(args)
        result = validator.is_valid()
        self.assertFalse(result)
        self.assertEqual(validator.error_message, "The argument 'arg1' is repeated.")
