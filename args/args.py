# pass list as arguments
def method1(arg1, arg2):
    print("method1", arg1, arg2)


list_args = [1, 'blah']
method1(*list_args)


# access arguments inside the method
def method2(*args):
    print("method2", args[0], args[1])


method2(1, 'blah')

list_args = [1, 'blah']
method2(*list_args)


# arguments and normal position parameters
def method3(arg1, *args):
    print("method3", arg1, args[0], args[1])


method3(1, 'blah', 'foo')

list_args = [1, 'blah', 'foo']
method3(*list_args)
