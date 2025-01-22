# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

def greeting(names, info):
    full_name = ""
    for name in names:
        full_name += f"{name} "
    full_name = full_name.strip()
    return f"Hello, {full_name}!  Nice to have a {info['title']} {info['occupation']} around."

print(greeting( ["John", "Q", "Doe"], {"title": "Master", "occupation": "Plumber"},))