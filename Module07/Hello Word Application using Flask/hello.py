from distutils.log import debug
from flask import Flask
app = Flask(__name__)

# @app.route(rule ,option )
@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    # app.run(host,port,debug,options)
    app.run()
