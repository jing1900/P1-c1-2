# -*- encoding=UTF-8 -*-
from flask_script import Manager
from c2 import app
'''这个文件存在的意义在于，当项目存在很多很多文件时，一一启动太麻烦，你可以在这里自己定义一些启动方式'''
manager = Manager(app)

'''这里可以放入参数，和参数的默认值'''
@manager.option('-n',  '--name', dest='name', default='nowcoder')
def hello(name):
    print('hello', name)

@manager.command
def initialize_database():
    'initialize database'
    print('database ...')

if __name__ == '__main__':
    manager.run()

'''使用时，可在终端先python manager.py
 python manager.py initialize_database

'''