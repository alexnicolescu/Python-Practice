import json


def get_birthdays():
    with open("birth.json", "r") as f:
        return json.load(f)


def add_entry():
    print(">>> Now find another scientist that will be save in the dictionary!")
    name = input(str("Name >>> "))
    birthday = input(str("Birthday >>> "))
    birthday_dict[name] = birthday
    with open("birth.json", "w") as f:
        json.dump(birthday_dict, f)


def find_date():
    name = str(input(">>> Who's birthday do you want to look up? >>> "))
    if name in birthday_dict:
        print(f"{name}'s birthday is {birthday_dict[name]}.")
    else:
        print(f"We don't have {name}'s birthday.")


def list_entries(birthday_dict):
    print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
    for key in birthday_dict.keys():
        print(key)


if __name__ == "__main__":
    birthday_dict = get_birthdays()
    list_entries(birthday_dict)
    find_date()
    add_entry()
