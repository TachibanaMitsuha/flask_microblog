from app import app

#两个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
    return 'hello world'