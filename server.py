from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/datas/<int:num>/')
def datas(num):
    return render_template('datas.html',num = num)


if __name__=="__main__":
    app.run(debug=True)