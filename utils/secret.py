import secrets
import hmac
import hashlib


class Secret:
    @staticmethod
    def generate_key(token_length: int) -> bytes:
        """
        Function generate a cryptographically secure random key (>= 256 bits)
        .
        :param token_length:
        :return:
        """
        return secrets.token_bytes(token_length if token_length >= 32 else 32)

    @staticmethod
    def generate_comp_choice(choices):
        """
        Function choose a random move for the computer

        :param choices:
        :return:
        """
        return secrets.choice(choices)

    @staticmethod
    def calculate_hmac(key, message):
        """
        Function calculate hmac with key, message and sha256

        :param key:
        :param message:
        :return:
        """
        h = hmac.new(key, message.encode("utf-8"), hashlib.sha256)
        return h.hexdigest()
