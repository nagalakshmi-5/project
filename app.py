from flask import Flask,render_template,request,session
import webbrowser
import mysql.connector as mysql
import matplotlib.pyplot as plt
app=Flask(__name__)
app.secret_key="chandu"
db=mysql.connect(
    host="localhost",
    user="root",
    password="Chandana@123",
    database="lucky"
)
cur=db.cursor()
@app.route("/")
def default():
    return render_template('home.html')
@app.route("/home")
def default1():
    return render_template('home.html')

@app.route("/details")
def details():
    return render_template('details.html')

@app.route('/submit',methods=['post'])
def submit():
    cusname=request.form['cusname']
    session['cusname']=cusname
    price=request.form['price']
    itemname=request.form['name']
    if(len(cusname)==0 or len(price)==0 or len(itemname)==0):
        return render_template('err1.html')
    sql="insert into balance(name,price,cusname) values(%s,%s,%s);"
    val=(itemname,price,cusname)
    cur.execute(sql,val)
    db.commit()
    sql4="select * from balance where cusname='"+session['cusname']+"';"
    cur.execute(sql4)
    res=cur.fetchall()
    db.commit()
    sum=0
    for i in res:
        b=int(i[1])
        sum=sum+b
    inc="select * from cust where name='"+cusname+"';"
    cur.execute(inc)
    res1=cur.fetchall()
    db.commit()
    for i in res1:
        b1=int(i[1])
    v=b1
    bal=0
    bal=v-sum
    return render_template('balance.html',i=v,e=sum,b=bal,n=cusname)


@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/submit1',methods=['post'])
def submit1():
    name=request.form['custname']
    income=request.form['income']
    phone=request.form['phone']
    session['cusname']=name
    if(len(name)==0 or len(income)==0 or len(phone)==0):
        return render_template('err1.html')
    if(len(phone)!=10):
        return render_template('err.html')
    sql2="select * from cust;"
    cur.execute(sql2)
    res=cur.fetchall()
    db.commit()
    for i in res:
        if i[0]==name:
            a=int(i[1])
            a+=int(income)
            sql3="update cust set income="+str(a)+" where name='"+name+"';"
            cur.execute(sql3)
            db.commit()
            return render_template('log1.html')
    else:
        sql1="insert into cust(name,income,phone) values(%s,%s,%s);"
        val=(name,income,phone)
        cur.execute(sql1,val)
        db.commit()
        return render_template('log.html')


@app.route('/getpie')
def getpie(): 
    sql="select * from balance where cusname='"+session['cusname']+"';"
    cur.execute(sql)
    res=cur.fetchall()
    db.commit()
    d=[]
    d1=[]
    for i in res:
        d.append(i[0])
    for i in res:
        d1.append(i[1])
    plt.pie(d1,labels=d,autopct='%.0f%%')
    plt.legend()
    plt.show()
    return 'data retrieved'
if __name__ == "__main__":
    app.run(debug=True)
