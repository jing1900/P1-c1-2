# -*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup

'''糗事百科爬虫'''
def qiushibaike():
    #获取内容
    content = requests.get('http://www.qiushibaike.com').content
    #解析
    soup = BeautifulSoup(content, 'html.parser')
    #打印
    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())

'''python string入门'''
def demo_string():
    stra = 'hello world'
    #变成首字母大写的标准形式
    print(stra.capitalize())
    #字符串替换
    print(stra.replace('world', 'nowcoder'))
    strb = '  \n\rhello nowcoder \r\n'
    #去除左边的空格回车等符号
    print(1, strb.lstrip())
    #去除右边的
    print(2, strb.rstrip())
    strc = 'hello w'
    #判断字符串是不是以这个开头结尾
    print(3, strc.startswith('hel'))
    print(4, strc.endswith('x'))
    #字符串连接
    print(5, stra + strb + strc)
    #字符串长度
    print(6, len(strc))
    #字符串连接
    print(7, '-'.join(['a', 'b', 'c']))
    #字符串连接
    print(8, strc.split(' '))
    #返回该字符串的首字母索引
    print(9, strc.find('ello'))

'''python 操作数入门'''
def demo_operation():
    print(1, 1 + 2, 5 / 2, 5 * 2, 5 - 2)
    print(2, True, not True)
    print(3, 1 < 2, 5 > 2)
    #位操作
    print(4, 2 << 3)
    #位操作
    print(5, 5 | 3, 5 & 3, 5 ^ 3)
    x = 2
    y = 3.3
    print(x, y, type(x), type(y))

'''Python行内函数入门'''
def demo_buildinfunction():
    #最大最小，绝对值，长度
    print(1, max(2, 1), min(5, 3))
    print(2, len('xxx'), len([1, 2, 3]))
    print(3, abs(-2))  # fabs,Math.fabs
    #python3,需要加list()
    print(4, list(range(1, 10, 3)))
    #dir，获取元素属性
    print(5, dir(list))
    x = 2
    #eval方法
    print(6, eval('x + 3'))
    #ascii编码转换
    print(7, chr(65), ord('a'))
    #得到除数余数
    print(8, divmod(11, 3))

'''python 控制流入门'''
def demo_controlflow():
    score = 65
    #if
    if score > 99:
        print(1, 'A')
    elif score > 60:
        print(2, 'B')
    else:
        print(3, 'C')
    #while
    while score < 100:
        print(score)
        score += 10
    score = 65

    #for
    # for (int i = 0; i < 10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_special
            # print(3, i
        if i < 5:
            continue
        print(3, i)
        if i == 6:
            break

'''python list 入门'''
def demo_list():
    #定义
    lista = [1, 2, 3]  # vector<int> Arraylist
    print(1, lista)
    #一个list可包含不同类型
    listb = ['a', 1, 'c', 1.1]
    print(2, listb)
    #拓展
    lista.extend(listb)
    print(3, lista)
    #长度
    print(4, len(lista))
    #判断元素是否在
    print(5, 'a' in listb)
    lista = lista + listb
    print(6, lista)
    #插入元素
    listb.insert(0, 'www')
    print(7, listb)
    #弹出元素
    listb.pop(1)
    print(8, listb)
    #反转列表
    listb.reverse()
    print(9, listb)
    print(10, listb[0], listb[1])
    #排序，一般需要列表中的元素为同一种
    #listb.sort()
    print(11, listb)
    #listb.sort(reverse=True)
    print(12, listb)
    #元素长度扩大两倍
    print(13, listb * 2)
    print(14, [0] * 14 ) # memset(src, 0, len))
    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print(15, listaa)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b

'''python 字典入门'''
def demo_dict():
    #定义
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print(1, dicta)
    #得到键，值
    print(2, dicta.keys(), dicta.values())
    #for key in dict:python 3
    #print(3, dicta.has_key(1), dicta.has_key('3'))
    # for map<int,int>::iterator it = x.begin(); it != x.end()
    for key, value in dicta.items():
        print('key-value:', key, value)
    #字典的值还可以是函数
    dictb = {'+': add, '-': sub}
    print(4, dictb['+'](1, 2))
    print(5, dictb.get('-')(15, 3))
    #字典赋值
    dictb['*'] = 'x'
    print(dictb)
    #弹出字典元素
    dicta.pop(4)
    print(6, dicta)
    #删除字典元素
    del dicta[1]
    print(7, dicta)

'''python 集合入门'''
def demo_set():
    lista = [1, 2, 3]
    #set定义
    seta = set(lista)
    setb = set((2, 3, 4))
    print(1, seta)
    #交
    print(3, seta.intersection(setb), seta & setb)
    #并
    print(4, seta | setb, seta.union(setb))
    #补
    print(5, seta - setb)
    #添加
    seta.add('x')
    print(6, seta)
    print(len(seta))
    #
    print(seta.isdisjoint(set((1, 2))))

'''python 封装 继承 多态'''
class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')

'''python 异常入门'''
def demo_exception():
    try:
        print(2 / 1)
        # print(2 / 0
        # if type == 'c':
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print('error:', e)
    finally:
        print('clean up')

'''python 随机数入门'''
def demo_random():
    # 1 - 100
    # random.seed(1)
    # x = prex * 100007 % xxxx
    # prex  = x 幂等性
    #1-100随机数
    print(1, int(random.random() * 100))
    #随机整数
    print(2, random.randint(0, 200))
    #选1
    print(3, random.choice(range(0, 100, 10)))
    #选4个
    print(4, random.sample(range(0, 100), 4))
    a = [1, 2, 3, 4, 5]
    #随机打乱
    random.shuffle(a)
    print(5, a)

'''python 正则表达式'''
def demo_re():
    str = 'abc123def12gh15'
    #1个多个数字
    p1 = re.compile('[\d]+')
    #1个数字
    p2 = re.compile('\d')
    print(1, p1.findall(str))
    print(2, p2.findall(str))
    # \t\n
    str = 'a@163.com;b@gmail.com;c@qq.com;e0@163.com;z@qq.com'
    #163，qq邮箱
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print(3, p3.findall(str))
    #中间是非<的内容
    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print(4, p4.findall(str))
    #只取中间的部分，返回不包含<h></h>
    p4 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print(5, p4.findall(str))
    #时间格式匹配
    str = 'xx2016-06-11yy'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print(p5.findall(str))


if __name__ == '__main__':
    qiushibaike()
    user1 = User('u1', 1)
    print(user1)
    admin1 = Admin('a1', 101, 'g1')
    print(admin1)

    print(create_user('USERX'))

    demo_string()
    demo_operation()
    demo_buildinfunction()
    demo_controlflow()
    demo_list()
    demo_dict()
    demo_set()
    demo_exception()
    demo_random()
    demo_re()
