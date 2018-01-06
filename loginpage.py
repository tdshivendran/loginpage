from flask import Flask, render_template,request, redirect, url_for

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Letmein@1', db='serverpage')
print(conn)
0
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

n = 1


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    uname = request.form['un']
    pswrd = request.form['pswrd']

    cursor=conn.cursor()
    query=("SELECT password FROM login WHERE username = %s")
    cursor.execute(query,(uname))
    result = cursor.fetchone()
    if pswrd == result[0]:
        return redirect(url_for('hello_world'))
    else:
        return result


@app.route('/signup', methods=['POST'])
def signup():
    username=str(request.form["un1"])
    password=str(request.form["pswrd1"])
    passrep=str(request.form["pswrdrep"])
    if password==passrep:
        global n
        n=n+1
        cursor = conn.cursor()

        query = ("INSERT INTO login VALUES (%s,%s,%s)")
        cursor.execute(query,(n,username,password))
        conn.commit()
        return "success"
    else:
        return "password mismatch"

if __name__ == '__main__':
    app.run()
