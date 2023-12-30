from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('pages/home.html')
 
@app.route('/login')
def login():
    return  render_template('pages/login.html')

@app.route('/register')
def register():
    return render_template('pages/register.html')
# @app.route('/register')
# def register():
#     return render_template('pages/register.html')

# @app.route('/doLogin',methods=['POST'])
# def do_login():
#     username = request.form['username']
#     password = request.form['psw']

#     if username == "manjul" and password == "manjul123":
#         return redirect('/')
#     else:
#         return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
