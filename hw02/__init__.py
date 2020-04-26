import check50

@check50.check()
def file_exists():
    """file exists"""
    check50.run("ls | grep hw02.c").stdout("hw02.c", regex=False).exit(0)

@check50.check()
def compiles():
    """compiles"""
    check50.run("gcc hw02.c").exit(0)

@check50.check()
def test_set_1():
    """test set 1"""
    check50.run("gcc hw02.c; ./a.out").stdin("1\n2\nq\n", prompt=False).stdout("You entered 2 integers.\n2 of the integers were positive.\n0 of the integers were negative.\nThe sum of the 2 integers was 3.\n", regex=False).exit(0)