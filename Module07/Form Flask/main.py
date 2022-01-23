from flask import Flask, render_template, request , url_for
app = Flask(__name__)

# @app.route(rule ,option )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email_id']
        password = request.form['password']
        if password =='admin':
            return render_template('dashboard.html',user = email.split('@')[0])
        else:
            return render_template('index.html',message="INVALID PASSWORD PLEASE ENTER AGAIN")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host,port,debug,options)
    app.run()
