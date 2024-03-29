# Read only property
# Raise an error inside of the setter method or leave out the setter completely


@property
def salary(self):
    return self.salary


@salary.setter
def salary(self, value):
    raise AttributeError("Salary is read only")
