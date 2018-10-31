class Sample:
    @property
    def do_something(self):
        return "Something has been done"

    @staticmethod
    def foo():
        print("La la la")


s = Sample()
# print(s.do_something())       # Invalid, as do_something is a property
print(s.do_something)           # do_something is treated as property which can be 'get'
# s.do_something = "some text"  # 'set' is invalid
s.foo()
type(s).foo()                   # Equivalent to Sample.foo()
Sample.foo()
