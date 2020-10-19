from flask import Flask, render_template

app = Flask(__name__,static_url_path='', static_folder='./static',
            template_folder='./templates')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cust')
def get_custs():
    return '<h1>customers</h1>'


@app.route('/stest')
def get_static():
    return render_template('a1.html')


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


@app.route('/t1')
def index2():
    user = {'username': 'user'}
    return render_template('t1.html', title='Home', user=user)


@app.route('/t2')
def index3():
    user = {'username': 'user'}
    return render_template('t2.html', title='Home', user=user)



if __name__ == '__main__':
    app.run()
