def welcome(name: str, greeting: str = "Hello"):
    print(f"{greeting}, World")
    print(f"I'm {name}.")


my_name = "Renner"
welcome(my_name)
welcome(my_name, "Bye")

# welcome()
# TypeError: welcome() missing 1 required positional argument: 'name'
# welcome("Renner", "Choi")
# TypeError: welcome() takes 1 positional argument but 2 were given
