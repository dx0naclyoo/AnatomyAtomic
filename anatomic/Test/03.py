
def func():
    var = 0

    def inner():
        nonlocal var
        var += 1
        print(var)

    return inner

f = func()

f()
f()
f()
