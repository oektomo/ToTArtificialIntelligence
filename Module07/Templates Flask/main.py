from flask import Flask, render_template
app = Flask(__name__)

# @app.route(rule ,option )
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet_name(name):
    return render_template('index.html',display = name)


if __name__ == "__main__":
    # app.run(host,port,debug,options)
    app.run()
