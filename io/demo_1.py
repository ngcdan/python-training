import os

print("----------------------------- List a directory ---------------------------------")


def list_dir(fld):
    for dir in os.listdir(fld):
        print(dir)


list_dir("/Users/linuss/Desktop")

print("----------------------------- Search file endWith | startWith ------------------------------------")


def search_file(fld, search_exp, search_type):
    for file in os.listdir(fld):
        if search_type == "endWith":
            if file.endswith(search_exp):
                print(file)
        elif search_type == "startWith":
            if file.startswith(search_exp):
                print(file)


search_file("./files", ".txt", "endWith")
