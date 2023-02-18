
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/mysite')
def my_site():
    return render_template('my_site.html')


@app.route('/show/<text>')
def show(text):
    some_list = [1,3,5,6,8,9,10]
    return render_template('show.html', title="from python", my_list = some_list, txt = text)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/child')
def child():
    return render_template('child.html')



if __name__ == '__main__':
    app.run(debug=True)



