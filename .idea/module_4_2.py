
def test_function(x):
    print('Я в области видимости функции test_function')
    a = x ** 2
    print(a)
    def  inner_function():
        nonlocal a
        a = a / 2
        print('Я в области видимости функции inner_function')
        print(a)
    inner_function()
    print(a)

test_function(5)
#inner_function()