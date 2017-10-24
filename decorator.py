#-*- encoding=UTF-8 -*-
'''装饰器'''
def log(level, *args, **kvargs):
    def inner(func):
        '''
        * 无名字参数，如果没有user = user,则放在这个数组里
        ** 有名字参数，否则，会放在kvargs
        '''

        def wrapper(*args, **kvargs):
            print(level, 'before calling ', func.__name__)
            print(level, 'args', args, 'kvargs', kvargs)
            func(*args, **kvargs)
            print(level, 'end calling ', func.__name__)

        return wrapper
    return inner


@log(level='INFO')
def hello(name, age):
    print('hello', name, age)

if __name__ == '__main__':
    hello(name='nowcoder', age=2) #= log(hello())