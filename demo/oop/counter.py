class Counter:
    # Constructor
    def __init__(self):
        # Object attribute
        self.value = 0

    # Methods
    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value


# Create an object of Counter class
c = Counter()
c.increment()
c.increment()
print(c.getvalue())
