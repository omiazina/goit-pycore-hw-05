from typing import List, Tuple
from colorama import init, Fore, Style

CONTACTS_STORAGE = {}

COLOR_COMMAND = Fore.CYAN
COLOR_DESCRIPTION = Fore.GREEN
COLOR_WELCOME = Fore.MAGENTA + Style.BRIGHT
COLOR_ERROR = Fore.RED
COLOR_RESPONSE = Fore.YELLOW

def input_error(func):
    def inner(args: List[str]) -> str:
        try:
            return func(args)
        except KeyError:
            return color_text("Contact not found.", COLOR_ERROR)
        except ValueError:
            return color_text("Give me name and phone please.", COLOR_ERROR)
        except IndexError:
            return color_text("Enter user name.", COLOR_ERROR)
    return inner


def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"


def color_print(text: str, color: str) -> None:
    print(color_text(text, color))


def print_menu() -> None:
    color_print("Available commands:", COLOR_WELCOME)
    color_print("  hello                 - Greet the assistant.", COLOR_COMMAND)
    color_print("  add [name] [phone]    - Add a new contact.", COLOR_COMMAND)
    color_print(
        "  change [name] [phone] - Change phone number of existing contact.",
        COLOR_COMMAND,
    )
    color_print("  phone [name]          - Show phone number of a contact.", COLOR_COMMAND)
    color_print("  all                   - Show all contacts.", COLOR_COMMAND)
    color_print("  exit, close           - Exit the assistant.", COLOR_COMMAND)


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def handle_hello(args: List[str]) -> str:
    return color_text("How can I help you?", COLOR_RESPONSE)

@input_error
def handle_add(args: List[str]) -> str:
    name, phone = args
    CONTACTS_STORAGE[name] = phone
    return color_text("Contact added.", COLOR_RESPONSE)

@input_error
def handle_change(args: List[str]) -> str:
    name, phone = args
    if name not in CONTACTS_STORAGE:
        raise KeyError()
    CONTACTS_STORAGE[name] = phone
    return color_text("Contact updated.", COLOR_RESPONSE)

@input_error
def handle_phone(args: List[str]) -> str:
    name = args[0]
    phone = CONTACTS_STORAGE[name]
    return color_text(phone, COLOR_RESPONSE)

@input_error
def handle_all(args: List[str]) -> str:
    if not CONTACTS_STORAGE:
        return color_text("No contacts saved.", COLOR_RESPONSE)
    lines = [
        f"{color_text(name, COLOR_COMMAND)}: "
        f"{color_text(phone, COLOR_RESPONSE)}"
        for name, phone in CONTACTS_STORAGE.items()
    ]
    return "\n".join(lines)


def main() -> None:
    init()  # for colorama (cross-platform color support)

    color_print("Welcome to the assistant bot!", COLOR_WELCOME)
    print_menu()

    command_handlers = {
        "hello": handle_hello,
        "add": handle_add,
        "change": handle_change,
        "phone": handle_phone,
        "all": handle_all,
    }

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            color_print("Good bye!", COLOR_WELCOME)
            break

        handler = command_handlers.get(command)
        if handler:
            print(handler(args))
        else:
            color_print("Invalid command.", COLOR_ERROR)

if __name__ == "__main__":
    main()
