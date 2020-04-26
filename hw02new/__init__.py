import check50
import check50.c

@check50.check()
def file_exists():
    """file exists"""
    check50.exists("hw02.c")

@check50.check()
def compiles():
    """compiles"""
    check50.c.compile("hw02.c", cc='gcc')

@check50.check()
def test_set_1():
    """test set 1"""
    check50.run("./hw02").stdin("1\n2\nq\n", prompt=False).stdout("You entered 2 integers.\n2 of the integers were positive.\n0 of the integers were negative.\nThe sum of the 2 integers was 3.\n", regex=False).exit(0)

@check50.check()
def test_set_2():
    """test set 2"""
    check50.run("./hw02").stdin("q", prompt=False).exit(0)