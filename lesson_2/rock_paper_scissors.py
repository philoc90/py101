import random


VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]


def convert_choice(choice):
    match choice:
        case "r":
            converted_choice = "rock"
        case "p":
            converted_choice = "paper"
        case "c":
            converted_choice = "scissors"
        case "l":
            converted_choice = "lizard"
        case "s":
            converted_choice = "spock"
        case _:
            converted_choice = choice
    return converted_choice


def prompt(message):
    print(f"==> {message}")


def display_winner(choice, computer_choice):
    prompt(f"You chose {choice}, computer chose {computer_choice}")
    if (
        (
            choice == "rock"
            and (computer_choice == "scissors" or computer_choice == "lizard")
        )
        or (
            choice == "paper"
            and (computer_choice == "rock" or computer_choice == "spock")
        )
        or (
            choice == "scissors"
            and (computer_choice == "paper" or computer_choice == "lizard")
        )
        or (
            choice == "lizard"
            and (computer_choice == "paper" or computer_choice == "spock")
        )
        or (
            choice == "spock"
            and (computer_choice == "scissors" or computer_choice == "rock")
        )
    ):
        prompt("You win!")
    elif (
        (
            choice == "rock"
            and (computer_choice == "paper" or computer_choice == "spock")
        )
        or (
            choice == "paper"
            and (computer_choice == "scissors" or computer_choice == "lizard")
        )
        or (
            choice == "scissors"
            and (computer_choice == "rock" or computer_choice == "spock")
        )
        or (
            choice == "lizard"
            and (computer_choice == "rock" or computer_choice == "scissors")
        )
        or (
            choice == "spock"
            and (computer_choice == "lizard" or computer_choice == "paper")
        )
    ):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")


keep_going = True
while keep_going:
    prompt(
        f"Choose one: {', '.join(VALID_CHOICES)}. (you may type the first letter of any choice instead.  Use s for spock and c for scissors.)"
    )
    choice = convert_choice(input().lower())

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = convert_choice(input().lower())

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
        if answer.startswith("n") or answer.startswith("y"):
            break
        else:
            prompt("That's not a valid choice")
    if answer[0] == "n":
        keep_going = False
