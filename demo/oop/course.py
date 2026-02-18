class Course:
    # static attribute
    taxrate = 15

    # static method
    @staticmethod
    def gettaxrate():
        return  Course.taxrate

    def __init__(self, title, fee):
        # Object attribute
        self.title = title
        self.fee = fee

    def show(self):
        print('Title : ',self.title)
        print('Fee   : ',self.fee)

    def getfee(self):
        return self.fee

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate / 100

c1 = Course("Gen AI", 10000)
c2 = Course("DS + ML", 9000)
print(c1.getnetfee())
print(Course.gettaxrate())

print(c1.__dict__)
print(Course.__dict__)

