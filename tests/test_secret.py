from unittest import TestCase
from utils.secret import Secret


class TestGenerateKey(TestCase):

    def test_generate_key_returns_bytes(self):
        key = Secret.generate_key(32)
        self.assertIsInstance(key, bytes)

    def test_generate_key_minimum_length(self):
        key = Secret.generate_key(16)
        self.assertIsInstance(key, bytes)
        self.assertEqual(len(key), 32)

    def test_generate_key_length_greater_than_32(self):
        key = Secret.generate_key(64)
        self.assertIsInstance(key, bytes)
        self.assertEqual(len(key), 64)


class TestGenerateCompChoice(TestCase):
    def test_generate_comp_choice(self):
        choices = ['rock', 'paper', 'scissors']
        comp_choice = Secret.generate_comp_choice(choices)
        self.assertIn(comp_choice, choices)
