# -*- encoding=UTF-8 -*-

from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

#定义app
app = Flask(__name__)
#加了这一行之后，在templates里面的语法，可以直接#开头
app.jinja_env.line_statement_prefix = '#'
#设置session之间相互通信的身份标识
app.secret_key = 'nowcoder'

#路径与函数的映射，这里路径可以是多个，因此，很适合改版的情况
@app.route('/index/')
@app.route('/')
def index():
    res = ''
    #这里获取通过flash传递的消息，其中category可以作为标识
    for msg, category in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'hello'
    return res

#这里我们用了前后端分离的策略，即前端的大部分代码放在templates里，只有少部分需要修改的参数，在这里传进去：render_template
#<int:uid>这里获取地址栏的参数,同时我们可以设置访问的类型，大小写都行
@app.route('/profile/<int:uid>/', methods=['GET', 'post'])
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)

#request，可以获取参数，如果没有就得到defaultkey
@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '++' + request.path + '<br>'
    #看request方法有什么属性
    for property in dir(request):
        res = res + str(property) + '<br>' + str(eval('request.' + property)) + '<br>'
    #response可以设置一些东西
    response = make_response(res)
    response.set_cookie('nowcoderid', key)
    response.status = '404'
    response.headers['nowcoder'] = 'hello~~'
    return response

#重定向后要跳转的路径
@app.route('/newpath')
def newpath():
    return 'newpath'

#访问它需要重定向的路径
@app.route('/re/<int:code>')
def redirect_demo(code):
    #跳转到新的路径，允许状态码
    return redirect('/newpath', code=code)

#错误页
@app.errorhandler(400)
def exception_page(e):
    response = make_response('出错啦~')
    return response

#404页，这里还可以返回找不到的url值
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url=request.url), 404

#测试
@app.route('/admin')
def admin():
    if request.args['key'] == 'admin':
        return 'hello admin'
    else:
        raise Exception()
#测试info log和flash传递消息
@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登陆成功', 'info')
    return 'ok'
    # return redirect('/')

#在页面中显示log等级
@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
    return 'logged:' + msg

#设置log，其中error的会出现在error，info和warn里，warn的会出现在warn和info里，info的只会出现在info里
def set_logger():
    info_file_handler = RotatingFileHandler('info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    set_logger()
    app.run(debug=True)
