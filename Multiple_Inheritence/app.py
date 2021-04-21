from promotable import Promotable
from salary import Salary

class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self):
        return self.calculate(40)

rolf = Employee(15.0)
print(rolf.weekly_salary())
rolf.promote(5.0)
print(rolf.weekly_salary())

bill = Employee(10.0)
print(bill.weekly_salary())
