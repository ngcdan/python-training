def find_acronym():
    look_up = input("What software acronym would you like to look up? \n")
    found = False
    try:
        with open("acronyms.txt", "r") as file:
            for line in file:
                if line.startswith(look_up):
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found: %s" % e)
        return

    if not found:
        print("No acronym found.")


def add_acronyms():
    acronym = input("What software acronym would you like to add? \n")
    definition = input("What is the definition? \n")
    with open("acronyms.txt", "a") as file:
        file.write(acronym + " - " + definition + "\n")


def main():
    # Ask the user whether they want to find or add an acronym
    choice = input("Do you want to find(F) or add(A) an acronym? \n")
    if choice == "F":
        find_acronym()
    else:
        add_acronyms()


main()
