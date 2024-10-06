def  test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()

#вне test_function, вызов inner_function выдает ошибку
