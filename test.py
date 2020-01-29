def test_args(normal_arg, *args):
    print("first normal arg: " + normal_arg)
    print(args)
    for arg in args:
        print("another arg through *args: " + arg)


test_args("normal", "python", "C++", "java")
