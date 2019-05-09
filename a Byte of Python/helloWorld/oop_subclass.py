class SchoolMemeber:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        """Tell my details."""
        print('Name : "{}" Age : "{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMemeber):
    """Represents a teacher."""
    def __init__(self, name , age, salary):
        SchoolMemeber.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{}'.format(self.name))

    def tell(self):
        SchoolMemeber.tell(self)
        print('Salary : "{:d}"'.format(self.salary))


class Student(SchoolMemeber):
    """Represents a student."""
    def __init__(self, name, age, marks):
        SchoolMemeber.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{}'.format(self.name))

    def tell(self):
        SchoolMemeber.tell(self)
        print('Marks : "{:d}"'.format(self.marks))


t = Teacher('Mr. Zhao', 40, 30000)
s = Student('huipengly', 24, 100)

# prints a blank line
print()

members = [t, s]
# 这里不是多态，只是list可以存不同的类型，然后每个类型都有tell
for member in members:
    # Works for both Teachers and Students
    member.tell()
