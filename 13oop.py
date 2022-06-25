Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class student:
    def __init__(self):
        self.marks=[]
    def print_marks(self):
        print(self,marks)
    def add_marks(self,mark):
        self.marks.append(mark)

        
s=student()
s.add_marks()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.add_marks()
TypeError: student.add_marks() missing 1 required positional argument: 'mark'
s.add_marks(30)
s.add_marks(40)
s.print_marks()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.print_marks()
  File "<pyshell#7>", line 5, in print_marks
    print(self,marks)
NameError: name 'marks' is not defined. Did you mean: 'vars'?
s.print_marks()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.print_marks()
  File "<pyshell#7>", line 5, in print_marks
    print(self,marks)
NameError: name 'marks' is not defined. Did you mean: 'vars'?
class student:
    def __init__(self):
        self.marks=[]
    def print_marks(self):
        print(self.marks)
    def add_marks(self,mark):
        self.marks.append(mark)

        
s1=student()
s1.print_marks()
[]
s1.add_marks(30)
s1.add_marks(90)
s1.add_marks(89)
s1.print_marks()
[30, 90, 89]
s1.marks()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1.marks()
TypeError: 'list' object is not callable
