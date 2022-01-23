from distutils.log import debug
from flask import Flask
app = Flask(__name__)

# @app.route(rule ,option )
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/greet')
def greeting():
    return "<h1>Good Morning!</h1>"   


@app.route('/greet/<name>')
def greeting_name(name):
    return f"<h1>Good Morning {name}!</h1>"   

if __name__ == "__main__":
    # app.run(host,port,debug,options)
    app.run()
