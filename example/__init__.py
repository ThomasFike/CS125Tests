import check50

@check50.check()
def file_exists():
    """file exists"""
    check50.run("ls | grep hello.py").stdout("hello.py", regex=False).exit(0)

@check50.check()
def testing_hello():
    """testing hello"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)