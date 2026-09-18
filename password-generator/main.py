from src.generator import PasswordGenerator
from src.ui import (
    print_banner,
    get_password_length,
    get_yes_no,
    render_password, 
    ask_generate_again
)

def main():
    print_banner()

    while True:
        #1. Collect User Preferences
        length = get_password_length()
        use_upper = get_yes_no("Include Uppercase Letters? (A-Z)")
        use_nums = get_yes_no("Include Numbers? (0-9)")
        use_syms = get_yes_no("Include Special Symbols? (!@#$)")

        #2. Generate Password
        generator = PasswordGenerator(
            length=length,
            use_uppercase=use_upper,
            use_numbers=use_nums,
            use_symbols=use_syms
        )
        password = generator.generate()
        strength = PasswordGenerator.evaluate_strength(password)

        #3. Output Result
        render_password(password, strength)

        #4. Check Replay Loop
        if not ask_generate_again():
            print("\nStay safe online! See you next time!\\n")
            break

if __name__ == "__main__":
    main()