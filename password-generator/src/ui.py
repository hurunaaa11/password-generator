import sys

CLR = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
CYAN = "\033[96m"

def print_banner():
    print(f"{CYAN}{'=' * 45}{CLR}")
    print(f"{BOLD}{GREEN} SECURE PASSWORD GENERATOR{CLR}")
    print(f"{CYAN}{'=' * 45}{CLR}\n")

def get_yes_no(prompt: str) -> bool:
    """Ask user a yes/no question."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print(f"{YELLOW} Please enter 'y' or 'yes' or 'n' for 'no'.{CLR}")

def get_password_length() -> int:
    """Gets valid length from user (minumum 6, maximum 64)."""
    while True:
        try: 
            length = int(input("Enter password length (8-64) [Default: 12]:") or 12)
            if 8 <= length <= 64:
                return length
            print(f"{YELLOW} Length must be between 8 and 64 characters.{CLR}")
        except ValueError:
            print(f"{RED} Invalid input!! Numbers only{CLR}")

def render_password(password: str, strength: str):
    print(f"{CYAN}{'=' * 45}{CLR}")
    print(f"{BOLD}Generated Password:{CLR} {GREEN}{password}{CLR}")
    print(f"{BOLD}Security Strength: {CLR} {strength}")
    print(f"{CYAN}{'=' * 45}{CLR}\n")

def ask_generate_again() -> bool:
    return get_yes_no("Would you like to generate another password?")