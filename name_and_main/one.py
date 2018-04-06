# whenever we call a python script directly python will assign the value '__main__' to a builtin function
# called __name__ . Hence developers use it to organize their code


def func():
    print("func() in one.py")

print("Top level in one.py")

if __name__ == '__main__':
    print("one.py is being run directly!")
else:
    print("one.py has been imported")
