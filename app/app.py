from flask import Flask
from flask import render_template
from sepwords import fenci
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/sep/', methods=['POST', 'GET'])
def sepSentence():
    if request.method == 'POST':
        sen = request.form['content']
        return sen
        

if __name__ == '__main__':
    #app.debug = True
    app.run()