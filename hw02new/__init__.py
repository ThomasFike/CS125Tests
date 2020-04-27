import check50
import check50.c

@check50.check()
def file_exists():
    """file exists"""
    check50.exists("hw02.c")

@check50.check(file_exists)
def compiles():
    """compiles"""
    check50.c.compile("hw02.c", cc='gcc')

@check50.check(compiles)
def test_set_1():
    """test set 1"""
    check50.run("./hw02").stdin("1\n2\nq\n", prompt=False).stdout("You entered 2 integers.\n2 of the integers were positive.\n0 of the integers were negative.\nThe sum of the 2 integers was 3.\n", regex=False).exit(0)

@check50.check(compiles)
def no_data():
    """q is used with no data entered"""
    check50.run("./hw02").stdin("q", prompt=False).exit(0)

@check50.check(compiles)
def large_data_set():
    """Very Large DataSet"""
    check50.run("./hw02").stdin("5884\n937\n-3532\n7223\n-7922\nq\n", prompt=True).stdout("You entered 5 integers.\n3 of the integers were positive.\n2 of the integers were negative.\nThe sum of the 5 integers was 2590.\n", regex=False).exit(0)

@check50.check(compiles)
def one_value():
    """one value"""
    check50.run("./hw02").stdin("256\nq\n", prompt=True).stdout("You entered 1 integers.\n1 of the integers were positive.\n0 of the integers were negative.\nThe sum of the 1 integers was 256.\n", regex=False).exit(0)
