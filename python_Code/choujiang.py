# 导入web框架
from flask import Flask, render_template
import random

# 创建应用对象
app = Flask(__name__)

# 创建一个包含人名的列表
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]

# 定义路由
@app.route('/index')
def index():
    return render_template('index.html', names=names)

# 定义抽奖路由
@app.route('/choujiang')
def choujiang():
    # 随机选取一个人名
    winner = names[random.randint(0, len(names)-1)]
    return render_template('index.html', names = names, winner=winner)

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
     

