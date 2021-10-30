from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/datas/<int:times>/<string:word>')
def datas(times, word):
    return render_template('datas.html',times = times, word = word)


if __name__=="__main__":
    app.run(debug=True)