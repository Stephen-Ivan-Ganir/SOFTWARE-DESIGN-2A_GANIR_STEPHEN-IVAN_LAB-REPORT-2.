import Student
from Student import Student
s = Student("Maria", 5)
print(s)
s.setScore(1, 100)
print(s)
s.setScore(2, 98)
print(s)
s.setScore(3, 95)
print(s)
s.setScore(4, 96)
print(s)
s.setScore(5, 99)
print(s)
print("\n")
print(s)
print("Average: " + str(s.getAverage()))


