def birthday(name):
    if name == "Ethan":
        return "9/16"
    elif name == "Rui":
        return "8/5"
    elif name == "Fiona":
        return  "9/28"
    else:
        return "I don't know"
def get_user_name():
    return input("please enter your name: ")
name = get_user_name()
#print(birthday("Ethan"))
print(f"My name is {name} and my birthday is {birthday(name)}")L