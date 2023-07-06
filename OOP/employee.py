######################################


class Employee1:
    pass


emp1_1 = Employee1()
emp1_2 = Employee1()

emp1_1.firstName = 'Fuzail'
emp1_1.lastName = 'Shareef'
fullname1_1 = '{} {}'.format(emp1_1.firstName, emp1_1.lastName)
print(fullname1_1)

emp1_2.firstName = 'Masood'
emp1_2.lastName = 'Khan'
fullname1_2 = '{} {}'.format(emp1_2.firstName, emp1_2.lastName)
print(fullname1_2)

# Instead of doing like above i.e. manually configuring all parameters
# of an employee, we can do somethings like this:


class Employee2:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        self.email = f'{first}.{last}@comapny.com'

    def fullName(self):
        return f'{self.firstName} {self.lastName}'


emp2_1 = Employee2('Fuzail', 'Shareef')
emp2_2 = Employee2('Masood', 'Khan')

print(emp2_1.fullName())
print(emp2_2.fullName())
