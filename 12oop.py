Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class A:
    def do(self):
        print('in A')

    
class B(A):
    pass

class c:
    def do(self):
        print('in c')

        
class D(c,B):
    pass

01=d()
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
1=D()
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=D()
1.do()
SyntaxError: invalid decimal literal
l.do()
in c
class f(B,c):
    pass

h=f()
h.do()
in A
print(D.mro())
[<class '__main__.D'>, <class '__main__.c'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
l.do()
in c
