def invalid_amount(amount):
    try:
        if float(amount) >= 0:
            return False
        return True
    except ValueError:
        return True


def invalid_duration(duration):
    try:
        int(duration)
    except ValueError:
        return True
    if int(duration) % 1 == 0 and int(duration) > 0:
        return False
    return True


def calculate_payment(apr, loan_amount, number_of_months):
    apr = float(apr)
    loan_amount = float(loan_amount)
    number_of_months = float(number_of_months)
    monthly_rate = (apr / 12) * 0.01
    try:
        monthly_payment = loan_amount * (
            monthly_rate / (1 - (1 + monthly_rate) ** (-number_of_months))
        )
    except ZeroDivisionError:
        monthly_payment = loan_amount / number_of_months

    return monthly_payment


def main():
    print("Welcome to mortgage calculator!")

    loan_amount = input("Please input the loan amount:$")
    while invalid_amount(loan_amount):
        loan_amount = input("Please input a positive number:$")

    apr = input("Please input the APR:%")
    while invalid_amount(apr):
        apr = input("Please input a positive APR:%")

    number_of_months = input("Please input the loan's duration in months: ")
    while invalid_duration(number_of_months):
        number_of_months = input("Please input the duration in months: ")

    monthly_payment = calculate_payment(apr, loan_amount, number_of_months)

    print(f"Your monthly payment is {monthly_payment:.2f}.")
    print(
        "Would you like to perform another calculation?  Enter y for yes, or anything else to exit."
    )
    answer = input().lower()
    if answer == "y":
        main()


main()
