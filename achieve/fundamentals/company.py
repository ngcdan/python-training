from employee import Employee


class Company:
    def __init__(self):
        self.employees = []

    def add_empl(self, employee):
        self.employees.append(employee)

    def display_name(self):
        for i in self.employees:
            print(i.fname, i.lname)
        print("--------------------")


def main():
    company = Company()

    empl1 = Employee("nqc", "dan", 1000)
    company.add_empl(empl1)
    print(company.display_name())


main()
