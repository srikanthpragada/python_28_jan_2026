from abc import ABC, abstractmethod

class Doctor(ABC):
    def __init__(self, name, mobile, dept):
        self.name = name
        self.mobile = mobile
        self.dept = dept

    def show(self):
        print(self.name, self.mobile, self.dept)

    @abstractmethod
    def getpay(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, mobile, dept, salary):
        super().__init__(name, mobile, dept)
        self.salary = salary

    def show(self):
        super().show()
        print(self.salary)

    def getpay(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, mobile, dept, visits, charge):
        super().__init__(name, mobile, dept)
        self.visits = visits
        self.charge = charge

    def show(self):
        super().show()
        print(self.visits, self.charge)

    def getpay(self):
        return self.visits * self.charge


c = Consultant("Dr. Dave", "93943434343", "ORTH", 10, 1500)
r = ResidentDoctor("Dr. James", "393493433", "CARD", 400000)

print(c.getpay())
print(r.getpay())
