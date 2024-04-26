from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/after10th')
def after10th():
    return render_template('after10th.html')


@app.route('/after12th')
def after12th():
    return render_template('after12th.html')


@app.route('/afterUG')
def afterUG():
    return render_template('afterUG.html')


@app.route('/exams')
def exams():
    return render_template('exams.html')


@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')

 
def create_connection():
    conn=sqlite3.connect('whatnext2.db')
    return conn

def create_table():
    conn=create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS USER(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usrnm TEXT NOT NULL,
                            email TEXT NOT NULL,
                            qualification TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        user=request.form['usrnm']
        email=request.form['email']
        qualification=request.form['qualification']
        print(user)
        print(email)
        print(qualification)
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO  USER(usrnm,email,qualification) VALUES(?,?,?)''',(user,email,qualification))
        conn.commit()
        conn.close()
        return "Registration Successfull"
    return render_template('register.html')
    
if __name__ == '__main__':
    create_table()
    app.run(debug=True)