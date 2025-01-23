# Currently, our calculator asks the user for two numbers and an operation and then exits after displaying the result. Wouldn't it be nice if we could ask the user if they wanted to perform another calculation and start a new calculation when they respond with yes?

# There are several messages sprinkled throughout the program. Can we move them into some configuration file and access them by key? That would let us manage the messages more easily, and we could even internationalize the messages.

# Your calculator program is a hit, and it's being used all over the world! The problem is, not everyone speaks English. You now need to internationalize the messages in your calculator. You've already done the hard work of extracting all the messages to a configuration file. Now, all you have to do is send that configuration file to translators and call the right translation in your code.

# Currently, our calculator only handles integer inputs. Let's modify it to accept floating-point numbers as well.

# to access messages in a config file, we need to import json
import json
# since at least one message is printed outside of the main function, we open the JSON file here-- i don't really know what this does yet
with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# all messages are now written as "messages['key in JSON file']"
prompt(messages['welcome'])

# to allow the user to perform another calculation, we turn the main block of code into a function called main() so that we can have it call itself at the end.
def main():
    prompt(messages['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(messages['invalid_number'])
        number1 = input()

    prompt(messages['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(messages['invalid_number'])
        number2 = input()

    prompt(messages['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages['invalid_operation'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    # because this message was originally formatted, and I don't know how to mix formatted strings and JSON files, I turned output from an into to a str and then concatenated it to the JSON message
    prompt(messages['result']+ str(output))
    # here is where we ask the user if they'd like to perform another calculation.  we confirm the input, and if they said y then we invoke main() and start from the beginning.  If they say n, we don't do anything and the program terminates.
    prompt(messages['new_calc'])
    answer = input()
    while answer != 'y' and answer != 'n':
        prompt(messages['invalid_answer'])
        answer = input()
    if answer == 'y':
        main()
main()