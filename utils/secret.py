import secrets


class Secret:
    #
    @staticmethod
    def generate_key(token_length: int) -> bytes:
        """
        Function generate a cryptographically secure random key (>= 256 bits)
        .
        :param token_length:
        :return:
        """

        return secrets.token_bytes(token_length if token_length >= 32 else 32)
