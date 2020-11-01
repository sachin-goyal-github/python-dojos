# pass dictionary as arguments
def method1(arg1, arg2):
    print("method1", arg1, arg2)


dict_args = {'arg1': 1, 'arg2': 'blah'}
method1(**dict_args)


# access keyword arguments inside the method
def method2(**kwargs):
    print("method2", kwargs['arg1'], kwargs['arg2'])


method2(arg1=1, arg2='blah')

dict_args = {'arg1': 1, 'arg2': 'blah'}
method2(**dict_args)


# keyword arguments and normal position parameters
def method3(arg1, **kwargs):
    print("method3", arg1, kwargs['arg2'], kwargs['arg3'])


method3(1, arg2='blah', arg3='foo')

dict_args = {'arg1': 1, 'arg2': 'blah', 'arg3': 'foo'}
method3(**dict_args)
