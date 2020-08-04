
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Elon', 'Musk', 200000000)
emp_2 = Employee('Bill', 'Gates', 150000000)

print(emp_1.fullname())
#Better approach
print(Employee.fullname(emp_2))
print(emp_2.pay)

emp_2.apply_raise()
print(emp_2.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.08
print(emp_1.raise_amount)
print(emp_2.raise_amount)