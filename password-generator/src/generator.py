import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate(self) -> str:
        """Generates a random password based on set criteria."""
        # Lowercase letters are always included as the base
        character_pool = string.ascii_lowercase

        # Guarantee at least one charachter from each selected set
        guaranteed_chars = [random.choice(string.ascii_lowercase)]

        if self.use_uppercase:
            character_pool += string.ascii_uppercase
            guaranteed_chars.append(random.choice(string.ascii_uppercase))

        if self.use_numbers:
            character_pool += string.digits
            guaranteed_chars.append(random.choice(string.digits))

        if self.use_symbols:
            character_pool += string.punctuation
            guaranteed_chars.append(random.choice(string.punctuation))

        # Fill the rest of the password length from the full character pool
        remaining_length = self.length - len(guaranteed_chars)
        remaining_chars = [random.choice(character_pool) for _ in range(remaining_length)]

        # Combine guaranteed chars + remaining_chars and shuffle them randomly
        full_password_list = guaranteed_chars + remaining_chars
        random.shuffle(full_password_list)

        return "".join(full_password_list)

    @staticmethod
    def evaluate_strength(password: str) -> str:
        """Calculates  password strength rating."""
        score = 0
        if len(password) >= 12: score += 1
        if len(password) >= 16: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Moderate"
        else:
            return "Strong"












