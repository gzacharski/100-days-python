def my_function():
    return 3 * 2


output = my_function()
print(output)


def format_name(first_name: str = "", last_name: str = ""):
    """
    Take a first and last name and format it to return
    the title case version of the name.
    """
    first_name_formatted = first_name.strip().lower().title()
    last_name_formatted = last_name.strip().lower().title()
    return f"{first_name_formatted} {last_name_formatted}"


print(format_name("GrzegorZ"))
