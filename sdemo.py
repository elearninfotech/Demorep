def f1():
    print('welcome')
    print(10/0)

try:
    f1()
except ZeroDivisionError:
    print('error')
    

