class Department:
    def __init__(self):
        self.fin = self.Finance()

    def display(self):
        print('In Department Class')

    class Finance:

        def display1(self):
            print("Finance class")


class Employee(Department):
    def __init__(self):
        print('In Subclass')
        super().__init__()

    class Finance(Department.Finance):

        def display2(self):
            print('Employee finance')

        # creating Sub_class object


a = Employee()
a.display()

# creating inner class object
b = a.fin
b.display1()
b.display2()


# adding some random changes
print(1)

