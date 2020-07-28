def get_birthdays():
    b_dict = {}
    with open("birthday.txt", "r") as f:
        for line in f:
            name, date = line.strip().split(':')
            b_dict[name] = date
    return b_dict

if __name__ == "__main__":
    birthday_dict = get_birthdays()
    print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
    for key in birthday_dict.keys():
        print(key)
    name = str(input(">>> Who's birthday do you want to look up? >>> "))
    if name in birthday_dict:
        print(f"{name}'s birthday is {birthday_dict[name]}.")
    else:
        print(f"We don't have {name}'s birthday.")
        