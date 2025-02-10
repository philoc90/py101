def print_in_box(message):
    print("+--" + ("-" * len(message)) + "+")
    print("| " + (" ")* len(message) + " |")
    print(f"| {message} |")
    print("| " + (" ")* len(message) + " |")
    print("+--" + ("-" * len(message)) + "+")
print_in_box('To boldly go where no one has gone before.')
