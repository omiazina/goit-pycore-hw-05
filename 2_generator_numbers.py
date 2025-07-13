import re

FLOAT_NUMBER_PATTERN = r'\b\d+\.\d+\b'  # matches floating-point numbers like 123.45

def generator_numbers(text):
    for match in re.findall(FLOAT_NUMBER_PATTERN, text):
        yield float(match)

def sum_profit(text, func):
    numbers = list(func(text))
    if not numbers:
        return 0.0
    return sum(numbers)

# def main():
#     text = (
#         "Загальний дохід працівника складається з декількох частин: "
#         "1000.01 як основний дохід, доповнений додатковими надходженнями "
#         "27.45 і 324.00 доларів."
#     )
#     total_income = sum_profit(text, generator_numbers)
#     print(f"Загальний дохід: {total_income}")

# if __name__ == "__main__":
#     main()
