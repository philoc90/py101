import random


VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WINNING_COMBOS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["scissors", "rock"],
}


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


def determine_round_winner(choice, computer_choice):
    if computer_choice in WINNING_COMBOS[choice]:
        round_winner = "player"
    elif choice in WINNING_COMBOS[computer_choice]:
        round_winner = "computer"
    else:
        round_winner = "nobody"
    return round_winner


def display_round_winner(round_winner, choice, computer_choice):
    prompt(f"You chose {choice}, computer chose {computer_choice}")
    match round_winner:
        case "player":
            prompt("You win the round!")
        case "computer":
            prompt("Computer wins the round!")
        case "nobody":
            prompt("This round is a tie!")


def determine_scores(round_winner, scores):
    match round_winner:
        case "player":
            scores[0] += 1
        case "computer":
            scores[1] += 1
    return scores


def display_overall_winner(scores):
    if scores[0] == 3:
        prompt("Player wins the match!")
    else:
        prompt("Computer wins the match!")


def main():
    keep_going = True
    while keep_going:
        scores = [0, 0]
        while scores[0] != 3 and scores[1] != 3:
            prompt(f"Choose one: {', '.join(VALID_CHOICES)}.")
            choice = convert_choice(input().lower())

            while choice not in VALID_CHOICES:
                prompt("That's not a valid choice")
                choice = convert_choice(input().lower())

            computer_choice = random.choice(VALID_CHOICES)
            round_winner = determine_round_winner(choice, computer_choice)
            display_round_winner(round_winner, choice, computer_choice)

            scores = determine_scores(round_winner, scores)
            prompt(
                f"The score is now player: {scores[0]}, computer: {scores[1]}."
            )
        display_overall_winner(scores)

        while True:
            prompt("Do you want to play again (y/n)?")
            answer = input().lower()
            if answer.startswith("n") or answer.startswith("y"):
                break
            prompt("That's not a valid choice")
        if answer[0] == "n":
            keep_going = False


main()
