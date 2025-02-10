# Write a function that takes a short line of text and prints it within a box.

# Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.

# For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.


def print_in_box(message, max_length=-1):
    print("+--" + ("-" * len(message[0:max_length])) + "+")
    print("| " + (" ")* len(message[0:max_length]) + " |")
    print(f"| {message[0:max_length]} |")
    print("| " + (" ")* len(message[0:max_length]) + " |")
    print("+--" + ("-" * len(message[0:max_length])) + "+")
print_in_box('To boldly go where no one has gone before.')
