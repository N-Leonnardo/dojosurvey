from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def success():
  return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    print (name)
    return 'Hi ' +name +'!'

@app.route('/repeat/<int:times>/<word>')
def repeat(times,word):
    i = 0
    words = ()
    while i < times:
        print(word)
        times -= 1
    return word



if __name__=="__main__":
    app.run(debug=True)