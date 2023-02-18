from flask import Flask, render_template, request, redirect

app = Flask(__name__)

text_list = []

@app.route('/', methods=['GET'])
def get_start():
    return render_template('index.html')


@app.route('/text/new', methods= ['GET'])
def text_new():
    return render_template('text_form.html')


@app.route('/display-text', methods= ['GET'])
def text():
    global text_list
    text_list.append(text_global)
    print(text_list)
    return render_template('text.html', data=text_global, all=text_list)


@app.route('/save', methods=['POST'])
def save():
    global text_global
    form = request.form
    text_global = form['text']


    print('Form text', text_global)
    return redirect('/display-text')




if __name__ == '__main__':
    app.run(debug=True)