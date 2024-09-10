from flask import Flask,redirect,url_for,render_template,jsonify,request
from flaskext.mysql import MySQL
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='student'
mysql=MySQL(app)
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    cursor=mysql.get_db().cursor()
    cursor.execute('select *from library')
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        id1=request.form['id']
        book_name=request.form['bookname']
        author_name=request.form['author']
        cursor=mysql.get_db().cursor()
        cursor.execute('insert into library(id,bookname,author) values(%s,%s,%s)',[id1,book_name,author_name])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('add.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        id1=request.form['id']
        book_name=request.form['bookname']
        author_name=request.form['author']
        cursor=mysql.get_db().cursor()
        cursor.execute('update library set bookname=%s,author=%s where id=%s',[book_name,author_name,id1])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        id1=request.form['id']
        cursor=mysql.get_db().cursor()
        cursor.execute('delete from library where id=%s',[id1])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('delete.html')
app.run(use_reloader=True)


